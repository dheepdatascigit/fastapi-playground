from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name: str):
    return f"welcome {name}"
    # return {"message": "Hello World"}

@app.get("/random/{end_num}")
async def random_number(end_num: int):
    result = randint(1, end_num)
    # return randint(1, end_num+1)
    return {"result": result}
