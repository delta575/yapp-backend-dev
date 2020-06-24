# yapp-backend-dev

> Yapp Backend Developer code challenge

This project demonstrates a simple implementation of a Serverless API that implements simple CRUD methods for a MySQL DataBase. It makes use of AWS SAM CLI deploying serverless functions as API endpoint handlers.

## Description

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- .env.example - A template that defines the project needed environment variables.
- template.yaml - A template that defines the application's AWS resources.
- docker-compose.yml - A containerized MySQL DataBase to help with fast deployment.
- yapp_backend/ - Code for the application's Lambda function.
  - tests/ - Unit tests for the application code.
  - app.py - Serverless API handlers.
  - db.py - Database connection and session setup.
  - models.py - Movie SQLAlchemy model.
  - data.csv - Kaggle data for movies and ratings.
  - seed.py - Script to populate blank DataBase.

## Requirements

This project assumes the following requirements are met.

- [Python3.7+ ](https://www.python.org/downloads/) - Lambda functions use Python runtime environment.
- [Docker and docker-compose](https://docs.docker.com/engine/install/) - Needed for AWS SAM CLI and MySQL DataBase.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) - AWS Serverless Application Model framework.

## Deployment

- ### Clone this repo

```bash

$ git clone https://github.com/delta575/yapp-backend-dev.git
$ cd yapp-backend-dev
```

- ### Set environment variables

Edit file following this specifications:

```bash
$ cp .env.example .env
$ nano .env
```

| Variable     | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| PYTHONPATH   | Changes python root path for SAM compatibility, must be changed to point at "yapp_backend" folder                                 |
| DATABASE_URL | MySQL URL for connection, must follow the following structure: "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}" |

**Important:**, set the same DATABASE_URL environment variable for SAM Global configs located on `template.yaml` file.

- ### Setup virtual environment and install requirements:

Install development requirements, poetry is used as the preferred package manager.

```bash
$ python -m pip install poetry
$ poetry install --dev
```

- ### Deploy MySQL DataBase

If you already have MySQL deployed you can skip this step, just make sure to point the DATABASE_URL env var correctly.
For easy deployment, a MySQL DataBase was containerized with a `docker-compose.yml` which also sets the needed environment variables for authentication.

```bash
$ docker-compose up -d
```

- ### Seed Data

Run the script `seed.py` which will create the Movie table from it's model and populate the DataBase with `data.csv` content.

```bash
$ python yapp_backend seed.py
```

- ### Run Unit Tests

Tests are defined in the `tests` folder in this project. Use [pytest](https://docs.pytest.org/en/latest/) to run unit tests.

```bash
poetry shell  # activate virtual environment
python -m pytests -v  # run unit tests
```

- ### Deploy SAM Local Server

```bash
sam build --use-container && sam local start-api
```

You can test the API visiting a GET method on your browser, by default SAM runs at [http://localhost:3000/](http://localhost:3000/).
[Postman](https://www.postman.com/) is recommended for fully featured testing.

## SAM API:

Simple CRUD methods:

| Method | Endpoint    | Description                                                        | Requires                               |
| ------ | ----------- | ------------------------------------------------------------------ | -------------------------------------- |
| GET    | /movie      | Returns Array of Movies                                            | None                                   |
| GET    | /movie/{id} | Returns movie matching id                                          | URL Params: movie id                   |
| POST   | /movie      | Creates new movie from JSON data on body of request                | Body: JSON with new movie data         |
| PUT    | /movie      | Updates movie title by id provided in JSON data on body of request | Body: JSON with movie id and new title |
| DELETE | /movie      | Removes Movie matching id of QueryString from DataBase             | QueryString: URL encoded movie id      |
