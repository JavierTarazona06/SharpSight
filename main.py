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
from data.SetSeller import SetSeller

#Users
from Models.User import User

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

class Users(BaseModel):
    id: Optional[int]
    nombre : str
    apellido : str
    email : str
    password : str


@app.get("/")
async def root():
    return {"message": "Welcome to SharpSight API. For API's documentation write in path ./docs/"}


#Users

@app.get("/user/validate/{cur_email}/{cur_password}", tags=["User"])
async def validate_user(cur_email:str, cur_password:str) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.post("/user/", tags=["User"])
async def create_user(in_user:Users) -> JSONResponse:
    try:
        cur_user = User(email=in_user.email, password=in_user.password, operation=2, name=in_user.nombre, last_name=in_user.apellido)
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.put("/user/{cur_email}/{cur_password}", tags=["User"])
async def modify_user(cur_email:str, cur_password:str, in_user:Users) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        cur_user.update(name=in_user.nombre, last_name=in_user.apellido, email=in_user.email, password=in_user.password)
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.delete("/user/{cur_email}/{cur_password}", tags=["User"])
async def delete_user(cur_email:str, cur_password:str) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        cur_user.delete()
        return {"Message": "Deleted successfully"}
    except Exception as e:
        return {"Error:" : str(e)}


#Results

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
@app.get("/wish_list/", tags=["Wish List"])
def show_wish_list() -> JSONResponse:
    try:
        wishListHeap_imp = WishListHeap()
        return wishListHeap_imp.view_whish_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.post("/wish_list/product", tags=["Wish List"])
def new_in_wish_list(product:Products) -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        whishListHeap_imp.insert(cur_product)
        return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {cur_product.titulo} ya que {e}"})

@app.delete("/wish_list/product", tags=["Wish List"])
def delete_in_wish_list(product:Products) -> JSONResponse:
    try:
        wishListHeap_imp = WishListHeap()
        cur_product = Product(title=product.titulo, price=product.precio, link=product.link, seller=product.tienda, image=product.imagen, brand=product.marca)
        wishListHeap_imp.delete(cur_product)
        return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto: {product.titulo} ya que no existe y/o {e}"})
    
@app.delete("/wish_list/max_product", tags=["Wish List"])
def delete_max_in_wish_List() -> JSONResponse:
    try:
        wishListHeap_imp = WishListHeap()
        prod_del = wishListHeap_imp.delete_max()
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
@app.get("/products/set/seller/{seller}", tags=["Set"])
def get_products_seller(seller:str) -> JSONResponse:
    try:
        mySet = SetSeller()
        return mySet.products_seller_json(seller)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: No hay tienda {e}"})
    
@app.get("/products/set/seller", tags=["Set"])
def get_sellers() -> JSONResponse:
    try:
        mySet = SetSeller()
        return mySet.sellers_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})