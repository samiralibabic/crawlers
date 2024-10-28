#!/bin/bash

SECRET_KEY="$1"
STRIPE_SECRET_KEY="$2"

cd /path/to/crawler || exit

git pull origin main || { echo "Git pull failed"; exit 1; }

docker-compose build || { echo "Build failed"; exit 1; }

docker-compose down

docker-compose up -d \
  -e SECRET_KEY="$SECRET_KEY" \
  -e STRIPE_SECRET_KEY="$STRIPE_SECRET_KEY" || { echo "Failed to start crawler"; exit 1; }

echo "Deployment complete for Crawler"