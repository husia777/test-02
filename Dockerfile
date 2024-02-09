# Dockerfile

FROM python:3.11


WORKDIR /app


RUN pip install poetry

 
COPY ./pyproject.toml ./


RUN poetry config virtualenvs.create false


RUN poetry install 
 
COPY . .


ENV PYTHONPATH "${PYTHONPATH}:/app/"

