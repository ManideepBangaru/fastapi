from fastapi import FastAPI, Body, Request

app = FastAPI()

@app.get("/")