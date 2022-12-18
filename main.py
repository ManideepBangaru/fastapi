from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/items/")
async def read_items(q : str = Query(default=... , min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# @app.get("/items/")
# async def read_items(q : str | None = Query(default = "fixedquery", min_length=3, max_length = 50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q : str | None = Query(default = None, min_length=3, max_length = 50, regex="[A-Z][a-z][0-5]")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(q : str | None = Query(default = None, min_length=3, max_length = 50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q : str | None = Query(default = None, max_length = 50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q:str | None=None):
#     results = {"items" : [{"item_id": "Foo"},{"item_id" : "bar"}]}
#     if q:
#         results.update({"q" : q})
#     return results

if __name__ == "__main__":
    uvicorn.run(app)