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
from data.WishListHeap import WishListHeap
from data.Product import Product
from data.ComparisonListAVL import ComparisonListAVL


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
    titulo: str
    precio : int
    link : Text
    tienda : Optional[str]
    imagen : Optional[Text]
    marca : Optional[str]


#Results

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products/{keyProd}", tags=["Products"])
def get_products_key(keyProd:str) -> JSONResponse:
    try:
        Search.Search(str(keyProd))
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/", tags=["Products"])
def get_products() -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/order/", tags=["Products"])
def get_products_order() -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.view_results_order()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/order_inverted/", tags=["Products"])
def get_products_orderInv() -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.view_results_orderInv()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/best_products/", tags=["Products"])
def get_best_products() -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.bestProduct_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/filter/greater/{price_min}", tags=["Products"])
def get_filter_products_greater(price_min:int) -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.filterGreater_json(price_min)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/filter/lower/{price_max}", tags=["Products"])
def get_filter_products_lower(price_max:int) -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.filterLower_json(price_max)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/filter/{price_min}/{price_max}", tags=["Products"])
def get_filter_products(price_min:int, price_max:int) -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.filter_json(price_min, price_max)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})


#WishList
@app.get("/whish_list/", tags=["Whish List"])
def show_whish_list() -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap()
        return whishListHeap_imp.view_whish_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.post("/whish_list/product", tags=["Whish List"])
def new_in_whish_list(product:Products) -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        whishListHeap_imp.insert(cur_product)
        return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {cur_product.titulo} ya que {e}"})

@app.delete("/whish_list/product", tags=["Whish List"])
def delete_in_whish_list(product:Products) -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        whishListHeap_imp.delete(cur_product)
        return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto: {product.titulo} ya que no existe y/o {e}"})
    
@app.delete("/whish_list/min_product", tags=["Whish List"])
def delete_min_in_whish() -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap()
        prod_del = whishListHeap_imp.delete_min()
        return JSONResponse(content={"message":f"Se eliminó el producto: {prod_del.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto con menor precio ya que {e}"})
    

#ComparisonList
@app.get("/comparison_list/", tags=["Comparison List"])
def show_comparison_list() -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        return comparison.view_comparison_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/comparison_list/order/", tags=["Comparison List"])
def show_ComparisonList_order() -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        return comparison.inOrder_JSON()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/comparison_list/order_inverted/", tags=["Comparison List"])
def show_ComparisonList_order_inverted() -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        return comparison.inOrderInv_JSON()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/comparison_list/comparison/", tags=["Comparison List"])
def show_ComparisonList_comparison() -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        return comparison.compareByPrice_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.post("/comparison_list/product", tags=["Comparison List"])
def new_in_comparison_list(product:Products) -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        comparison.insert(cur_product)
        return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {cur_product.titulo} ya que {e}"})
    
@app.delete("/comparison_list/product", tags=["Comparison List"])
def delete_in_comparison_list(product:Products) -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        comparison.delete(cur_product)
        return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title}"})
    except Exception as e:
        print(e)
        return JSONResponse(content={f"message":f"No se eliminó el producto: {product.titulo} ya que no existe y/o {e}"})
    

#Set by seller
