FROM python:{{ cookiecutter.minimal_python_version }}-slim

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-dev --no-interaction --no-ansi

COPY ./{{ cookiecutter.service_name }}  /code/{{ cookiecutter.service_name }}/

ENV LOGURU_AUTOINIT 0
