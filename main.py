from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def say_hello():
    return {"Hello":"World !!!"}