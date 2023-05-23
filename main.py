# from fastapi import FastAPI

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
    #Exito.searchProduct("reloj samsung a4")
    #Search.Search("Iphone 14")


    myImplementationDLL = generalResultsImplementation()
    print(myImplementationDLL)
    print("--------")
    #myImplementationDLL.filterGreater(5000000)
    #print(myImplementationDLL)

    print("-------")

    #wishList = WishList()
    #wishList.insert(myImplementationDLL.list_data.head.key)
    #wishList.delete()
    #wishList.delete()
    #print(wishList)

    comparisonList = ComparisonList()
    #comparisonList.insert(myImplementationDLL.list_data.head.next.next.key)
    #comparisonList.delete(2)
    print(comparisonList)
    print("-------")
    print(comparisonList.compareByPrice())

    #menu.startMenu()

__init__()
