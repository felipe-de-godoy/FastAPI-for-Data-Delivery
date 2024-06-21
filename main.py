from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()

# Estrutura dos dados
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Banco de dados fictício (em memória)
fake_db: List[Item] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.get("/items/", response_model=List[Item])
async def get_items():
    return fake_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    # Verifica se o item já existe
    for existing_item in fake_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    fake_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for idx, existing_item in enumerate(fake_db):
        if existing_item.id == item_id:
            fake_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

#   comando para criar item
#    curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "description": "This is item 1"}'
#    curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 2, "name": "Item 2", "description": "This is item 2"}'
# comando atualizar item
# curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item 1", "description": "This is the updated item 1"}'




