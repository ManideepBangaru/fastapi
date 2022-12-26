from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.background import BackgroundTasks
import time

app = FastAPI()

list_of_usernames = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def handle_email_background(email : str, data : str):
    print(email)
    print(data)
    for i in range(100):
        print(i)
        time.sleep(0.1)

@app.get("/users/email")
async def handle_email(email : str , background_task : BackgroundTasks):
    print(email)
    background_task.add_task(handle_email_background, email, "This is a sample background task manager")
    return {"user" : "Manideep", "message" : "Mail Sent"}

@app.post("/token")
async def token_generate(form_data : OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username, "token_type":"bearer"}

@app.post("/users/profilepic")
async def profile_pic(token : str = Depends(oauth2_scheme)):
    print(token)
    return {"User" : "Manideep","profile_pic" : "My_face"}