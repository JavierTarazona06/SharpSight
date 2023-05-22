from fastapi import FastAPI

import Scrapping.MercadoLibre
import Scrapping.Ktronix
from Scrapping import Exito
import menu
from data import *
from data.ComparaisonList import ComparisonList
from Scrapping import *

'''
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

'''


def __init__():
    #menu.startMenu()
    #Scrapping.MercadoLibre.searchProduct("Iphone 12")
    #Scrapping.Ktronix.searchProduct("motorola g52")
    Exito.searchProduct("reloj samsung a4")


__init__()
