#!/usr/bin/env bash
set -e

ENV=${1:-dev}
shift

export DJANGO_SETTINGS_MODULE=core.settings.$ENV

exec poetry run "$@"
