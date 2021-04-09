from fastapi import FastAPI
from pydantic import BaseModel
#import maths
import string_s 
from typing import Optional 

app = FastAPI()

@app.get("/")
async def read_root():
    return { "greating":"hello world"}


@app.get("/string_lenght/{my_string}")
async def string_lenght(my_string: str):
    count = 0
    try:
        while my_string[count]:
            count += 1
    except:        
        return {"my_string_len": count}

@app.get("/string_generator/{str_lenght}")
async def string_generator(str_lenght: int):
    string = ''
    while str_lenght > 0:
        string += input()
        str_lenght -= 1
    return {"generated_string": string}       