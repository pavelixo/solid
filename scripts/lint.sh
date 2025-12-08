#!/usr/bin/env bash

set -e
set -x

poetry run isort .
poetry run black .
poetry run flake8 .