from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name : str
    description : str | None
    price : float
    tax : float | None

app = FastAPI()

# @app.post("/items/")
# async def create_item(item : Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price with tax" : price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id : int, item : Item):
#     return {"item_id" : item_id, **item.dict()}

@app.put("/items/{item_id}")
async def create_item(item_id : int, item : Item, q : str | None = None):
    result = {"item_id" : item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result

if __name__ == "__main__":
    uvicorn.run(app)