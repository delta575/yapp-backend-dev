from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from db import Base


class Movie(Base, SerializerMixin):
    """Movie model for mysqlachemy
    Valid JSON data example:
        {
        "title": "Elizabeth",
        "genres": "Biography,Drama,History",
        "age": "18+",
        "country": "United Kingdom",
        "directors": "Shekhar Kapur",
        "disney_plus": "0",
        "movie_type": "0",
        "year": "1998",
        "hulu": "0",
        "language": "English,French",
        "rotten_tomatoes": "82%",
        "imbd": "7.4",
        "netflix": "1",
        "prime_video": "0",
        "runtime": "124"
    }
    """

    __tablename__ = "movies"
    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String(length=300))
    year = Column("Year", String(length=50))
    age = Column("Age", String(length=10))
    imbd = Column("IMDb", String(length=10))
    rotten_tomatoes = Column("Rotten Tomatoes", String(length=10))
    netflix = Column("Netflix", String(length=10))
    hulu = Column("Hulu", String(length=10))
    prime_video = Column("Prime Video", String(length=10))
    disney_plus = Column("Disney+", String(length=10))
    movie_type = Column("Type", String(length=10))
    directors = Column("Directors", String(length=500))
    genres = Column("Genres", String(length=300))
    country = Column("Country", String(length=300))
    language = Column("Language", String(length=300))
    runtime = Column("Runtime", String(length=10))

    _csv_columns = [
        "index",
        "id",
        "title",
        "year",
        "age",
        "imbd",
        "rotten_tomatoes",
        "netflix",
        "hulu",
        "prime_video",
        "disney_plus",
        "movie_type",
        "directors",
        "genres",
        "country",
        "language",
        "runtime",
    ]
