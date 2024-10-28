#!/bin/bash

SECRET_KEY="$1"
STRIPE_SECRET_KEY="$2"

REPO_URL="https://github.com/samiralibabic/crawlers.git"

if [ ! -d /home/crawler ]; then
    mkdir -p /home/crawler
fi
cd /home/crawler || exit

if [ ! -d .git ]; then
    echo "Cloning repository for the first time..."
    git clone "$REPO_URL" . || { echo "Git clone failed"; exit 1; }
else
    echo "Pulling latest changes from repository..."
    git pull origin main || { echo "Git pull failed"; exit 1; }
fi

docker-compose build || { echo "Build failed"; exit 1; }
docker-compose down

export SECRET_KEY="$SECRET_KEY"
export STRIPE_SECRET_KEY="$STRIPE_SECRET_KEY"

docker-compose up -d || { echo "Failed to start crawler"; exit 1; }

echo "Deployment complete for Crawler"
