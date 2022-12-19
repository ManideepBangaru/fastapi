from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

class User(BaseModel):
    username : str
    fullname : str | None = None

# Multiple body parameters
@app.put("/items/{item_id}")
async def update_items(item_id : int, item1 : Item, user : User, importance : int = Body()):
    results = {"item_id" : item_id, "item" : item1, "user" : user, "importance" : importance}
    return results

# # Multiple body parameters
# @app.put("/items/{item_id}")
# async def update_items(item_id : int, item1 : Item, user : User):
#     results = {"item_id" : item_id, "item" : item1, "user" : user}
#     return results

# @app.put("/items/{item_id}")
# async def update_item(*,\
#     item_id:int = Path(title="The id of the item to get", ge=0, le=1000),
#     q : str | None = None,
#     item : Item | None = None):
#     results = {"item_id" : item_id}
#     if q:
#         results.update({"q" : q})
#     if item:
#         results.update({"item" : item})
#     return results

if __name__ == "__main__":
    uvicorn.run(app)