from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/fastapi_app/items/{item_id}")
async def read_item(item_id : str, q : str | None = None, short : bool = False):
    item = {"item" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update({"description" : "This is an amazing item that has a long description"})
    return item

@app.get("/fastapi_app/users/{user_id}/items/{item_id}")
async def read_user_item(user_id : int, item_id : str, q : str | None = None, short : bool = False):
    item = {"item_id" : item_id, "owner_id" : user_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update({"description" : "This is an amazing item that has a long description"})
    return item

@app.get("/fastapi_app/names/{name_id}")
async def read_user_name(name_id : int, needy : str):
    users = {"user_id" : name_id, "user_name" : needy}
    return users

if __name__ == "__main__":
    uvicorn.run(app)