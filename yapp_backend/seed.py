import csv

from db import Base, Session, engine
from models import Movie


def seed_data(file_path):
    """Populates MySQL DataBase with data from csv file
    Format should follow this Kaggle example:
    https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney/data#
    """
    # Create Schema
    Base.metadata.create_all(engine)

    # Create SQL Session
    session = Session()

    # Read csv file and add data to session
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)  # skip headers
        columns = Movie()._csv_columns
        for row in reader:
            movie_data = {key: val for key, val in zip(columns, row)}
            movie_data.pop("index")
            session.add(Movie(**movie_data))

    session.commit()
    session.close()


if __name__ == "__main__":
    seed_data("yapp_backend/data.csv")
