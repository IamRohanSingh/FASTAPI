from fastapi import FastAPI
from pydantic import BaseModel
import maths
from typing import Optional 

app = FastAPI()

@app.get("/")
async def read_root():
    return { "greating":"hello world"}

@app.get("/fibonacci/{number}")
async def calculate_fibonacci(number: int):
    return {"number": maths.fibonacci(number)}

@app.get("/factorial/{value}")
async def calculate_factorail(value: int): 
    return {"n": maths.factorial(value)}

       
    




       