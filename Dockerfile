# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/

RUN pip install poetry

RUN poetry install# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy requirements file to inventory_management_system directory
COPY inventory_management_system/pyproject.toml /inventory_management_system/

# install dependencies

RUN poetry install --no-interaction --no-dev

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/


# command to run on container start
CMD ["poetry", "run", "python", "inventory_management_system/main.py"]