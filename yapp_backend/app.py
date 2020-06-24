import functools
import json
import logging

from db import Session
from models import Movie

log = logging.getLogger(__name__)


def handler_decorator(handler):
    """Response Handler decorator
    Catches errors and handle sessions
    """

    @functools.wraps(handler)
    def handler_wrapper(event, context):
        try:
            session = Session()
            data = handler(event, context, session)

            response = {"statusCode": 200}

            if data:
                response["body"] = json.dumps({"data": data})

            return response

        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"error": e.args})}

        finally:
            session.close()

    return handler_wrapper


@handler_decorator
def movie_list_handler(event, context, session):
    """GET /movie/list Handler
    Returns:
    JSON with list of all movies
    """
    movies = session.query(Movie).order_by(Movie.title).all()
    return [movie.to_dict() for movie in movies]


@handler_decorator
def movie_get_handler(event, context, session):
    """GET /movie/{id} Handler
    Returns:
    JSON with movie matching URL id parameter
    """
    movie_id = event["pathParameters"]["id"]

    movie = session.query(Movie).get(movie_id)

    return movie.to_dict() if movie else None


@handler_decorator
def movie_create_handler(event, context, session):
    """POST /movie Handler
    Request Body:
    JSON following Movie model
    Returns:
    JSON with new movie added to DB
    """
    payload = json.loads(event["body"])

    new_movie = Movie(**payload)

    session.add(new_movie)
    session.commit()

    return new_movie.to_dict()


@handler_decorator
def movie_update_handler(event, context, session):
    """PUT /movie Handler
    Request Body:
    JSON following containing Movie id and new title. example:
    {
        "id": 3,
        "title": "Star Wars"
    }
    Returns:
    JSON with modified movie data
    """
    payload = json.loads(event["body"])
    movie_id = payload.pop("id")

    movie = session.query(Movie).get(movie_id)
    movie.title = payload["title"]
    session.commit()

    return movie.to_dict()


@handler_decorator
def movie_delete_handler(event, context, session):
    """DELETE /movie?id={id} Handler
    URL Params:
    Query String containing Movie id to delete, example:
    ?id=153
    Returns:
    Status code of resulting operation
    """
    movie_id = event["queryStringParameters"]["id"]

    session.query(Movie).filter(Movie.id == movie_id).delete()
    session.commit()

    return None
