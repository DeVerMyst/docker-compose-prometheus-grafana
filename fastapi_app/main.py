from fastapi import FastAPI, Form
from loguru import logger
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}

@app.post("/data")
async def receive_color(data: str = Form(...)):
    logger.info(f"Received data: {data}")
    return {"message": f"data {data} received"}