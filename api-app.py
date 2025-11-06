from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

app = FastAPI(title="Items API", description="A simple CRUD API for managing items", version="1.0.0")

# Pydantic models for data validation
class Item(BaseModel):
    """Item model with ID, name, and description"""
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)

class ItemCreate(BaseModel):
    """Model for creating a new item (without ID)"""
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)

class ItemUpdate(BaseModel):
    """Model for updating an item"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)

# In-memory data store with 10 creative sample items
items_db: List[Item] = [
    Item(id=1, name="Quantum Coffee Mug", description="A mug that keeps your coffee in a superposition of hot and cold until observed"),
    Item(id=2, name="Invisible Ink Pen", description="Perfect for writing secret messages that only appear under moonlight"),
    Item(id=3, name="Self-Folding Laundry Basket", description="Uses advanced origami algorithms to fold your clothes automatically"),
    Item(id=4, name="Telepathic Keyboard", description="Types what you're thinking before you even touch it"),
    Item(id=5, name="Time-Traveling Alarm Clock", description="Wakes you up yesterday so you're never late"),
    Item(id=6, name="Gravity-Defying Bookshelf", description="Books float in mid-air, organized by color and reading level"),
    Item(id=7, name="Mood Ring Mouse Pad", description="Changes color based on your stress level during work"),
    Item(id=8, name="Infinite Loop Scarf", description="A scarf with no beginning or end, perfect for cold weather"),
    Item(id=9, name="Binary Bubble Wrap", description="Each pop plays a different bit of your favorite song"),
    Item(id=10, name="Schrödinger's Lunch Box", description="Contains both your lunch and not your lunch until opened")
]

# Helper function to get the next available ID
def get_next_id() -> int:
    """Generate the next available ID for a new item"""
    if not items_db:
        return 1
    return max(item.id for item in items_db) + 1

# Helper function to find an item by ID
def find_item_by_id(item_id: int) -> Optional[Item]:
    """Find an item in the database by its ID"""
    return next((item for item in items_db if item.id == item_id), None)

# API Endpoints

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint to verify the API is running"""
    return {
        "status": "healthy",
        "message": "Items API is up and running",
        "version": "1.0.0"
    }

@app.get("/items", response_model=List[Item], status_code=status.HTTP_200_OK)
async def get_all_items():
    """Retrieve all items from the in-memory store"""
    return items_db

@app.get("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def get_item(item_id: int):
    """Retrieve a specific item by its ID"""
    item = find_item_by_id(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item and add it to the store"""
    new_item = Item(
        id=get_next_id(),
        name=item.name,
        description=item.description
    )
    items_db.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_item(item_id: int, item_update: ItemUpdate):
    """Update an existing item by its ID"""
    item = find_item_by_id(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    # Update only the fields that were provided
    if item_update.name is not None:
        item.name = item_update.name
    if item_update.description is not None:
        item.description = item_update.description
    
    return item

if __name__ == "__main__":
    # Run the application using uvicorn on port 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)
