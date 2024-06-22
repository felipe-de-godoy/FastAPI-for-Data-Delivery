```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
uvicorn main:app --reload
aws sts get-caller-identity
eksctl create cluster --name=minimal-cluster --region=us-east-1 --nodegroup-name=minimal-nodes --node-type=t3.micro --nodes=1 --nodes-min=1 --nodes-max=2 --node-volume-size=10 --managed
aws ecr create-repository --repository-name my-fastapi-app --region us-east-1
docker build -t my-fastapi-app .
docker tag my-fastapi-app:latest 836090608262.dkr.ecr.us-east-1.amazonaws.com/my-fastapi-app:latest
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 836090608262.dkr.ecr.us-east-1.amazonaws.com
docker push 836090608262.dkr.ecr.us-east-1.amazonaws.com/my-fastapi-app:latest
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 1. Adicionar um Novo Item (POST)

Para adicionar um novo item à lista:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "description": "This is item 1"}'
```

### 2. Tentar Adicionar um Item com Mesmo ID (POST)

Para verificar se a API retorna um erro ao tentar adicionar um item com um ID que já existe:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Another Item 1", "description": "This should fail"}'
```

### 3. Atualizar um Item Existente (PUT)

Para atualizar um item na lista:
```sh
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item 1", "description": "This is the updated item 1"}'
```

### 4. Verificar se a Atualização Funcionou (GET)

Para verificar se a atualização foi bem-sucedida:
```sh
curl -X GET "http://127.0.0.1:8000/items/1"
```

### 5. Adicionar Outro Novo Item (POST)

Para adicionar outro item, com um ID diferente, para garantir que a API continua funcionando corretamente:
```sh
curl -X POST "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/" -H "Content-Type: application/json" -d '{"id": 2, "name": "Item 2", "description": "This is item 2"}'
```

### 6. Listar Todos os Itens (GET)

Para listar todos os itens e verificar o estado atual do banco de dados em memória:
```sh
curl -X GET "http://a4c687170ef9043c78ff390877622a8a-333739630.us-east-1.elb.amazonaws.com/items/"
```

### 7. Tentar Atualizar um Item que Não Existe (PUT)

Para tentar atualizar um item que não existe na lista e verificar se a API retorna um erro 404:
```sh
curl -X PUT "http://127.0.0.1:8000/items/3" -H "Content-Type: application/json" -d '{"id": 3, "name": "Non-existent Item", "description": "This should fail"}'
```