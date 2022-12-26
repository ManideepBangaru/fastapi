from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

list_of_usernames = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_generate(form_data : OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username, "token_type":"bearer"}

@app.post("/users/profilepic")
async def profile_pic(token : str = Depends(oauth2_scheme)):
    print(token)
    return {"User" : "Manideep","profile_pic" : "My_face"}