#!/bin/bash

# Navigate to the project directory
cd /home/web-crawlers

# Pull the latest changes from the repository
git pull origin main

# Build the Docker image
docker build -t web-crawler-app .

# Stop the existing container
docker stop web-crawler-app || true
docker rm web-crawler-app || true

# Run the Docker container with environment variables
docker run -d -p 80:5001 --name web-crawler-app -e STRIPE_SECRET_KEY=$STRIPE_SECRET_KEY -e SECRET_KEY=$SECRET_KEY web-crawler-app