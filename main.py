from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

class UserIn(BaseModel):
    username : str
    password : str
    email : EmailStr
    full_name : str | None = None

class UserOut(BaseModel):
    username : str
    email : EmailStr
    full_name  : str | None = None

class Item(BaseModel):
    Name : str
    Description : str | None = None
    Price : float
    tax : float | None = None
    tags : list[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item : Item):
    return item

@app.post("/user/", response_model=UserOut)
async def create_user(user : UserIn):
    return user

if __name__ == "__main__":
    uvicorn.run(app)