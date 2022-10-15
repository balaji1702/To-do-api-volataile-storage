from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str  = None
    price: float
    tax: float = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str  = None):
    result = item.dict()

    print(item_id)
    print(item)
    if q:
        result.update({"q": q})
    return result
