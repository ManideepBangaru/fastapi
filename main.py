from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

# @app.get("/items/")
# async def read_items(q : str | None = Query(default=None, min_length = 3, max_length=50, regex="^fixedquery$")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str = Query(min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str | None = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# ---------------------------   Query parameter list / multiple values -------------------

# @app.get("/items/")
# async def read_items(q: list[str] | None = Query(default=None)):
#     query_items = {"q": q}
#     return query_items

# --------------- Query parameter list / multiple values with defaults -------------------

@app.get("/items/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

if __name__ == "__main__":
    uvicorn.run(app)