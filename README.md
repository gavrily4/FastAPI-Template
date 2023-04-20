# FastAPI Template Project
This project is a template for quickly starting a web application using the FastAPI Python framework. The template includes the latest technologies, libraries, and best practices. To create this template, I have researched many papers, Stack Overflow topics, and watched numerous video tutorials.

## Technologies Used
+ FastAPI
+ PostgreSQL
+ Alembic
+ SQLAlchemy 2.0

## Getting Started
To use this template, follow these steps:

1. Clone the repository
2. Run the command `pip install -r requirements.txt` in the source directory
3. Build docker containers using `docker-compose build`
4. Run containers using `docker-compose up -d`

## Running application
+ http://127.0.0.1:8000/ - backend main page.
+ http://127.0.0.1:8000/docs - backend swagger documentation.
+ http://127.0.0.1:3000/ - frontend.

## Migrations
To make migrations with the database running in docker:

1. Create a migration using `docker-compose run backend_service alembic revision --autogenerate -m "First migration"`
2. Upgrade the database using `docker-compose run backend_service alembic upgrade head`

## Credits
+ FastAPI: https://fastapi.tiangolo.com/
+ PostgreSQL: https://www.postgresql.org/
+ Alembic: https://alembic.sqlalchemy.org/en/latest/
+ SQLAlchemy: https://www.sqlalchemy.org/

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.