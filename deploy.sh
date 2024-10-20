#!/bin/bash

# Navigate to the project directory
cd /home/crawler

# Pull the latest changes from the repository
git pull origin main

# Build the Docker image
docker build -t crawler .

# Stop the existing container
docker stop crawler || true
docker rm crawler || true

# Run the Docker container with environment variables
docker run -d -p 5001:5001 --name crawler \
  -e STRIPE_SECRET_KEY="$STRIPE_SECRET_KEY" \
  -e SECRET_KEY="$SECRET_KEY" \
  crawler

# Print container logs
docker logs crawler
