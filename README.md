### 1. Adicionar um Novo Item (POST)

Para adicionar um novo item à lista:
```sh
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "description": "This is item 1"}'
```

### 2. Tentar Adicionar um Item com Mesmo ID (POST)

Para verificar se a API retorna um erro ao tentar adicionar um item com um ID que já existe:
```sh
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Another Item 1", "description": "This should fail"}'
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
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 2, "name": "Item 2", "description": "This is item 2"}'
```

### 6. Listar Todos os Itens (GET)

Para listar todos os itens e verificar o estado atual do banco de dados em memória:
```sh
curl -X GET "http://127.0.0.1:8000/items/"
```

### 7. Tentar Atualizar um Item que Não Existe (PUT)

Para tentar atualizar um item que não existe na lista e verificar se a API retorna um erro 404:
```sh
curl -X PUT "http://127.0.0.1:8000/items/3" -H "Content-Type: application/json" -d '{"id": 3, "name": "Non-existent Item", "description": "This should fail"}'
```