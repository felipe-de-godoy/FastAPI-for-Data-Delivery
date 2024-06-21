# Dockerfile
# Use the official Python image from the Docker Hub

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./main.py /app/main.py


# Set the working directory inside the Docker container
WORKDIR /app

# Copy the requirements.txt file into the Docker image
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your FastAPI code into the Docker image
# COPY . .

# Expose the port your FastAPI app runs on (default is 8000)
# EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]