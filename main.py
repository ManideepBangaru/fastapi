from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import uvicorn

app = FastAPI()

# image url
class Image(BaseModel):
    url : HttpUrl
    name : str

class Item(BaseModel):
    name : str
    description : str | None
    price : float
    tax : float | None = None
    tags : set[str] = set()
    images : list[Image] | None = None

@app.put("/items/{item_id}")
async def read_item(item_id : int, item : Item):
    results = {"item_id" : item_id, "item" : item}
    return results


# General way - image url
# class Image(BaseModel):
#     url : str
#     name : str

# class Item(BaseModel):
#     name : str
#     description : str | None
#     price : float
#     tax : float | None = None
#     tags : set[str] = set()
#     image : Image | None = None

# @app.put("/items/{item_id}")
# async def read_item(item_id : int, item : Item):
#     result = {"item_id" : item_id, "item" : item}
#     return result


# Python has a specific way to declare lists with internal types or "type parameters"
# class Item(BaseModel):
#     name : str
#     description : Union[str, None] = None
#     price : float
#     tax : float
#     tags : List[str] = []

# @app.put("/items/{item_id}")
# async def read_item(item_id : int, item : Item):
#     results = {"item id" : item_id, "item" : item}
#     return results

# General way
# class Item(BaseModel):
#     name : str
#     description : str
#     price : float
#     tax : float
#     tags : list = []

# @app.put("/items/{item_id}")
# async def update_item(item_id : int, item: Item):
#     results = {"item_id":item_id, "item" : item}
#     return results

if __name__ == "__main__":
    uvicorn.run(app)