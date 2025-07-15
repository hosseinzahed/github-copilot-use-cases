from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

""" Prompt in Ask/Edit/Agent:
Generate a fast api application with the following endpoints:
- GET / : Show a health check message.
- GET /items: Retrieve a list of all items.
- GET /items/{item_id}: Retrieve an item by its ID.
- POST /items: Create a new item.
- PUT /items/{item_id}: Update an existing item by its ID.

The application should use a simple in-memory data store (a list) to manage the items with 10 creative sample items.
The item should have an ID, a name, and a description.
Use Pydantic for data validation and serialization.
Include appropriate status codes and error handling.
Use the FastAPI framework for building the API.
Run the application using uvicorn on port 8080.
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Health check OK"}

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items = [
    Item(id=1, name="Item 1", description="A unique item with special properties."),
    Item(id=2, name="Item 2", description="An ancient artifact with historical significance."),
    Item(id=3, name="Item 3", description="A modern gadget with cutting-edge technology."),
    Item(id=4, name="Item 4", description="A rare collectible from a distant land."),
    Item(id=5, name="Item 5", description="A handcrafted piece of art."),
    Item(id=6, name="Item 6", description="A vintage item with a rich history."),
    Item(id=7, name="Item 7", description="A futuristic device with advanced features."),
    Item(id=8, name="Item 8", description="A mysterious object with unknown origins."),
    Item(id=9, name="Item 9", description="A limited edition item with high value."),
    Item(id=10, name="Item 10", description="A classic item with timeless appeal."),
]

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

