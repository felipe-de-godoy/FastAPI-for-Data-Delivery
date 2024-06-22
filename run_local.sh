#!/bin/bash
set -e

# Variables
DOCKER_IMAGE_NAME="my-fastapi-app"

# Step 1: Build Docker image
echo "Building Docker image..."
docker build -t $DOCKER_IMAGE_NAME .

# Step 2: Run Docker container locally
echo "Running Docker container locally..."
docker run -d -p 8000:8000 --name my-fastapi-container $DOCKER_IMAGE_NAME

# Optional: Display Docker container logs (uncomment if needed)
# echo "Displaying Docker container logs..."
# docker logs -f my-fastapi-container

echo "FastAPI application is now running at http://localhost:8000"

# Instructions to stop the container
echo "To stop the container, run: docker stop my-fastapi-container"
echo "To remove the container, run: docker rm my-fastapi-container"