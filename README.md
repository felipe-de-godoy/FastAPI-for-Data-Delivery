# FastAPI Application Deployment

This guide provides steps to set up a FastAPI application locally using Python and to deploy it on AWS using EKS and ECR.

## Local Setup

### 1. Upgrade `pip` and Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt 
```

### 2. Run FastAPI Locally

```bash
uvicorn main:app --reload
```

## Local with Docker

### 1. Make the Shell Script Executable

```bash
chmod +x run_local.sh
```

### 2. Run the Shell Script

```bash
./run_local.sh
```

## Deploying on AWS

### 3. Verify AWS CLI Configuration

Ensure your AWS CLI is configured correctly by running:

```bash
aws sts get-caller-identity
```

### 4. Create an EKS Cluster

```bash
eksctl create cluster --name=minimal-cluster --region=us-east-1 --nodegroup-name=minimal-nodes --node-type=t3.micro --nodes=1 --nodes-min=1 --nodes-max=2 --node-volume-size=10 --managed
```

### 5. Create an ECR Repository

```bash
aws ecr create-repository --repository-name my-fastapi-app --region us-east-1
```

### 6. Build and Tag Docker Image

```bash
docker build -t my-fastapi-app .
docker tag my-fastapi-app:latest <your-account>.dkr.ecr.us-east-1.amazonaws.com/my-fastapi-app:latest
```

### 7. Log in to ECR

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-account>.dkr.ecr.us-east-1.amazonaws.com
```

### 8. Push Docker Image to ECR

```bash
docker push <your-account>.dkr.ecr.us-east-1.amazonaws.com/my-fastapi-app:latest
```

### 9. Apply Kubernetes Deployment and Service

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 10. Check Deployment and Services Status

```bash
kubectl get deployments
kubectl get services
```

## API Usage

### 1. Add a New Item (POST)

To add a new item to the list:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "description": "This is item 1"}'
```

### 2. Try to Add an Item with the Same ID (POST)

To check if the API returns an error when trying to add an item with an existing ID:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Another Item 1", "description": "This should fail"}'
```

### 3. Update an Existing Item (PUT)

To update an item in the list:
```sh
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item 1", "description": "This is the updated item 1"}'
```

### 4. Verify the Update (GET)

To verify if the update was successful:
```sh
curl -X GET "http://127.0.0.1:8000/items/1"
```

### 5. Add Another New Item (POST)

To add another item with a different ID to ensure the API continues to function correctly:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 2, "name": "Item 2", "description": "This is item 2"}'
```

### 6. List All Items (GET)

To list all items and check the current state of the in-memory database:
```sh
curl -X GET "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/"
```

### 7. Try to Update a Non-existent Item (PUT)

To attempt to update an item that does not exist in the list and check if the API returns a 404 error:
```sh
curl -X PUT "http://127.0.0.1:8000/items/3" -H "Content-Type: application/json" -d '{"id": 3, "name": "Non-existent Item", "description": "This should fail"}'
```
