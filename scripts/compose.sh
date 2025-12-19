#!/usr/bin/env bash

ENV=${1:-dev}

docker compose \
  -f docker/compose/${ENV}.docker-compose.yml \
  up --build --remove-orphans
