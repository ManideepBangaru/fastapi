from enum import Enum
from fastapi import FastAPI
import uvicorn

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/fastapi_app/sayhello")
async def say_hello():
    return "Hello World !!!"

@app.get("/fastapi_app/sayhello/{name}")
async def say_hello_name(name:str):
    return "Hello %s !!!"%name

@app.get("/fastapi_app/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name}
    
    if model_name.value == "lenet":
        return "model name is len %s"%model_name
    
    return "model name %s"%model_name

if __name__ == "__main__":
    uvicorn.run(app)