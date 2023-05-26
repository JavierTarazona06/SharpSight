# from fastapi import FastAPI

from fastapi import FastAPI, Body, HTTPException, Path, Query, Request, Depends
#return html
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from pydantic import Field
#Valores por defecto y opcionales
from typing import Optional, List, Union, Text
#Validaciones
from starlette.responses import JSONResponse
#Tokens
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder

from data import Results


app = FastAPI()
app.title = "Sharp Sight Backend"
app.version = "1.0.0"

#Models

class Products(BaseModel):
    title: str
    price : int
    link : Text
    brand : str
    image : Optional[Text]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/products/{key_word}", tags=["Products"])
def get_products_key(key_word:str) -> JSONResponse:
    impDLL = Results.generalResultsImplementation()
    products = impDLL.list_data
    print(products)
    result = []
    if products.isEmpty():
        return result
    else:
        headRef = products.head
        while headRef.next is not None:
            result.append(headRef.key.json())
            headRef = headRef.next
        result.append(headRef.key.json())
        return result