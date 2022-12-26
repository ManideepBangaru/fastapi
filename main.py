from fastapi import FastAPI, Body, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json

app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ping test
@app.get("/ping")
def home():
    return "Ping"

# define login page
@app.post("/token")
def login(form_data : OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    with open("userdb.json") as json_file:
        json_data = json.load(json_file)
    if json_data:
        # check if the username is present
        password = json_data.get(form_data.username)
        if not password:
            print("User not authenticated !!!, please Re-Enter")
            raise HTTPException(status_code=403, detail="Incorrect Password")
    # To check if user is in the db and password matches or not
    return {"access_token" : form_data.username, "token_type":"bearer"}

@app.get("/spend/history")
def spend_history(token:str=Depends(oauth_scheme)):
    # spend history logic
    print("Spend History")