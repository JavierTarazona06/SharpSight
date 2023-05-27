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
#Cors: All origins can have access
from fastapi.middleware.cors import CORSMiddleware
from data import ResultsAVL
from Scrapping import Search

#Data Structures
from data import Results
from data.Node import Node


app = FastAPI()
app.title = "Sharp Sight Backend"
app.version = "1.0.0"

#Cors config.
origins = ["*"]  # Configura aquí los orígenes permitidos

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/products/", tags=["Products"])
def get_products() -> JSONResponse:
    impDLL = Results.generalResultsImplementation()
    products = impDLL.list_data
    result = []
    if products.isEmpty():
        return result
    else:
        headRef : Node = products.head
        while headRef.next is not None:
            result.append(headRef.key.json())
            headRef = headRef.next
        result.append(headRef.key.json())
        return result
    
@app.get("/products/{keyProd}", tags=["Products"])
def get_products_key(keyProd:str) -> JSONResponse:
    Search.Search(keyProd)
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    return resulAVL_imp.preOrder_JSON()