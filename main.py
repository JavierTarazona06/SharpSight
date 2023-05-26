# from fastapi import FastAPI
from fastapi import FastAPI

import Scrapping.MercadoLibre
import Scrapping.Ktronix
from Scrapping import Search
from Scrapping import Exito
import menu
from data import *
from data.ComparaisonList import ComparisonList
from Scrapping import *
from Scrapping import *
from data.Results import generalResultsImplementation
from data.WishList import WishList


app = FastAPI()
app.title = "Sharp Sight Backend"
app.version = "1.0.0"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}