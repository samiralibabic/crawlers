#!/bin/bash

SECRET_KEY="$1"
STRIPE_SECRET_KEY="$2"

cd /home/crawler || exit

git pull origin main || { echo "Git pull failed"; exit 1; }

docker-compose build || { echo "Build failed"; exit 1; }

docker-compose down

export SECRET_KEY="$SECRET_KEY"
export STRIPE_SECRET_KEY="$STRIPE_SECRET_KEY"

docker-compose up -d || { echo "Failed to start crawler"; exit 1; }

echo "Deployment complete for Crawler"
