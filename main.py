from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/fastapi_app/sayhello")
async def say_hello():
    return "Hello World !!!"

@app.get("/fastapi_app/sayhello/{name}")
async def say_hello_name(name:str):
    return "Hello %s !!!"%name

if __name__ == "__main__":
    uvicorn.run(app)