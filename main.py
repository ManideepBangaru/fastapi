from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/fastapi_app")
async def say_hello():
    return "Hello World !!!"

if __name__ == "__main__":
    uvicorn.run(app)