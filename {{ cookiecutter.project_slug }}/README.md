# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

# Development

## Installing dependencies

This project uses [poetry 1.1.3](http://python-poetry.org) for its dependency management. If you don't have poetry installed please, install it via the following command:

```console
$ POETRY_VERSION=1.1.3 curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

To install dependencies please use the following command:

```console
poetry install
```

## Code formatting

To format code you can use [pre-commit](http://pre-commit.com).

Firstly, you need to install pre-commit hooks:

```console
$ pre-commit install
```

Then you can run code format:

```console
$ pre-commit run --all-files
```

These hooks will also be executed before every commit.


## Project structure:

```
├── docker                          <- Files related to deployment via docker
│   └── Dockerfile
├── tests                           <- Folder for tests of this application
├── {{ cookiecutter.service_name }} 
    ^--------------------------------- Name of main module in snake case
│   ├── __init__.py                 <- Says that folder is module
│   ├── errors.py                   <- Custom errors implementation
│   ├── log.py                      <- Loguru sink and formatter
│   ├── main.py                     <- Main file with configuration
│   ├── py.typed                    <- This file marks module as typed
│   └── settings.py                 <- File that loads configurations into settings object
├── .env.sample                     <- Excample of .env file. You can use it to set environment variables.
│                                      (You can setup usage of env variables by copying it into file with name .env)
├── .gitignore                      <- List of files for git to ignore
├── pyproject.toml                  <- Dependencies and settings of black and isort tool. execute in console `poetry install` to install them. `poetry add LIB_NAME` to add new dependency.
├── README.md                       <- file you are reading
├── CHANGELOG.md                    <- File that describes notable changes of this project
├── .flake8                         <- Settings for flake8
└── mypy.ini                        <- Settings for mypy
```

# About original template

Repository created from [churnikov:cookiecutter-python](https://github.com/churnikov/cookiecutter-python) using template version [{% gitcommit %}](https://github.com/churnikov/cookiecutter-python/commit/{% gitcommit %}).
