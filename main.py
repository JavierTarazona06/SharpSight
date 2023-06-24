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
from data import GraphProducts
from data.WishListsHash import WishListsHash
from data.UserWhListHash import UserWListHash

#Users
from Models.user import User

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
    nombre : str = Field(default=None)
    apellido : str = Field(default=None)
    email : str = Field(default=None)
    password : str = Field(default=None)


@app.get("/")
async def root():
    return {"message": "Welcome to SharpSight API. For API's documentation write in path ./docs/"}

#Global Variables
user_active = {"active":None}

#Users

@app.get("/user/", tags=["User"])
async def validate_user(cur_email:str, cur_password:str) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        user_active["active"] = cur_user
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.get("/user/session", tags=["User"])
async def session_user() -> JSONResponse:
    try:
        if user_active["active"]:
            return user_active["active"].json()
        else:
            return {"Error" : "No se ha iniciado sesión"}    
    except Exception as e:
        return {"Error" : str(e)}
    
@app.put("/user/log_out", tags=["User"])
async def log_out_user() -> JSONResponse:
    if user_active["active"]:
        user_active["active"] = None
        return {"mesage" : "Se ha cerrado la sesión"} 
    else:
        return {"mesage" : "No hay sesión iniciada"} 
    
@app.post("/user/", tags=["User"])
async def create_user(email, password, nombre, apellido) -> JSONResponse:
    try:
        cur_user = User(email=email, password=password, operation=2, name=nombre, last_name=apellido)
        user_active["active"] = cur_user
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.put("/user/", tags=["User"])
async def modify_user(cur_email:str, cur_password:str, in_user:Users) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        cur_user.update(name=in_user.nombre, last_name=in_user.apellido, email=in_user.email, password=in_user.password)
        user_active["active"] = cur_user
        return cur_user.json()
    except Exception as e:
        return {"Error:" : str(e)}
    
@app.delete("/user/", tags=["User"])
async def delete_user(cur_email:str, cur_password:str) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        cur_user.delete()
        user_active["active"] = None
        return {"Message": f"Usuario con email {cur_email} eliminado exitosamente"}
    except Exception as e:
        return {"Error:" : str(e)}


#Results

@app.get("/product/", tags=["Products"])
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
    
@app.get("/products/filter/", tags=["Products"])
def get_filter_products_greater(price_min:int=None, price_max:int=None) -> JSONResponse:
    try:
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        if price_min and price_max:
            return resulAVL_imp.filter_json(price_min, price_max)
        elif not price_min:
            return resulAVL_imp.filterLower_json(price_max)
        elif not price_max:
            return resulAVL_imp.filterGreater_json(price_min)
        else:
            return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/products/filter/seller/", tags=["Products"])
async def get_products__by_seller(sellers:str=None) -> JSONResponse:
    #sellers is a str separeted by '_'
    try:
        if not sellers is None:
            graph_implementation = GraphProducts.graph_implementation()
            return graph_implementation.get_products_seller(sellers)
        else:
            resulAVL_imp = ResultsAVL.results_AVL_imp()
            return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/products/filter/brand/", tags=["Products"])
async def get_products__by_brand(brands:str=None) -> JSONResponse:
    #brands is a str separeted by '_'
    try:
        if not brands is None:
            graph_implementation = GraphProducts.graph_implementation()
            return graph_implementation.get_products_brand(brands)
        else:
            resulAVL_imp = ResultsAVL.results_AVL_imp()
            return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

#WishList

@app.get("/wish_list/", tags=["Wish List"])
def show_wish_list_by_id(id:int) -> JSONResponse:
    try:
        wish_lists_imp = WishListHeap(id)
        return wish_lists_imp.view_whish_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.post("/wish_list/product", tags=["Wish List"])
def new_in_wish_list(wish_list_id:int, titulo, precio, link, tienda, imagen, marca) -> JSONResponse:
    try:
        whishListHeap_imp = WishListHeap(wish_list_id)
        cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
        whishListHeap_imp.insert(cur_product)
        return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title} en la lista {wish_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {titulo} ya que {e}"})

@app.delete("/wish_list/product", tags=["Wish List"])
def delete_in_wish_list(wish_list_id:int, titulo, precio, link, tienda, imagen, marca) -> JSONResponse:
    try:
        wishListHeap_imp = WishListHeap(wish_list_id)
        cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
        wishListHeap_imp.delete(cur_product)
        return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title} en la lista {wish_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto: {titulo} ya que no existe y/o {e}"})
    
@app.delete("/wish_list/max_product", tags=["Wish List"])
def delete_max_in_wish_List(wish_list_id:int) -> JSONResponse:
    try:
        wishListHeap_imp = WishListHeap(wish_list_id)
        prod_del = wishListHeap_imp.delete_max()
        return JSONResponse(content={"message":f"Se eliminó el producto: {prod_del.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto con menor precio ya que {e}"})
    

#List of Wish Lists

@app.post("/wish_list/", tags=["Wish List"])
def post_wish_list(name:str=None) -> JSONResponse:
    wish_lists_hashTable = WishListsHash()
    wish_list_id = wish_lists_hashTable.create(name, [])
    return JSONResponse(content={"message":f"Lista creada exitosamente con ID: {wish_list_id}"})

@app.get("/wish_list/id", tags=["Wish List"])
def wish_list_by_name(name:str) -> JSONResponse:
    try:
        wish_lists_hashTable = WishListsHash()
        wish_list_id = wish_lists_hashTable.find_id(name)
        return JSONResponse(content={"ID":wish_list_id})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/wish_list/name", tags=["Wish List"])
def wish_list_by_id(id:int) -> JSONResponse:
    try:
        wish_lists_hashTable = WishListsHash()
        wish_list_name = wish_lists_hashTable.find_name(str(id))
        return JSONResponse(content={"Name":wish_list_name})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.put("/wish_list/name", tags=["Wish List"])
def update_wish_list_name(id, new_name:str) -> JSONResponse:
    wish_lists_hashTable = WishListsHash()
    wish_list_name = wish_lists_hashTable.update_name(id, new_name)
    return JSONResponse(content={"message":f"Nombre actualizado exitosamente a {new_name}"})
    
@app.delete("/wish_list/", tags=["Wish List"])
def delete_wish_list_by_id(id:int) -> JSONResponse:
    try:
        wish_lists_hashTable = WishListsHash()
        wish_lists_hashTable.delete_wish_list(id)
        return JSONResponse(content={"message":f"Wish list con id {id} eliminada con exito"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})


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
def new_in_comparison_list(titulo, precio, link, tienda, imagen, marca) -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
        comparison.insert(cur_product)
        return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {titulo} ya que {e}"})
    
@app.delete("/comparison_list/product", tags=["Comparison List"])
def delete_in_comparison_list(titulo, precio, link, tienda, imagen, marca) -> JSONResponse:
    try:
        comparison = ComparisonListAVL()
        cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
        comparison.delete(cur_product)
        return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title}"})
    except Exception as e:
        print(e)
        return JSONResponse(content={f"message":f"No se eliminó el producto: {titulo} ya que no existe y/o {e}"})
    
@app.get("/sellers", tags=["Other"])
def get_sellers() -> JSONResponse:
    try:
        graph_implementation = GraphProducts.graph_implementation()
        return graph_implementation.get_sellers()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/brands", tags=["Other"])
def get_brands() -> JSONResponse:
    try:
        graph_implementation = GraphProducts.graph_implementation()
        return graph_implementation.get_brands()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})


@app.get("/brands/seller", tags=["Other"])
def get_brands_by_seller(sellers:str=None) -> JSONResponse:
    #Sellers is a str separated by '_'
    try:
        graph_implementation = GraphProducts.graph_implementation()
        if not sellers is None:
            graph_implementation = GraphProducts.graph_implementation()
            return graph_implementation.get_brands_sellers(sellers)
        else:
            print(graph_implementation.get_sellers()["tiendas"])
            tiendas_raw:list = graph_implementation.get_sellers()["tiendas"]
            n_tiendas = len(tiendas_raw)
            sellers = ""
            for i in range(len(tiendas_raw)):
                if i == n_tiendas -1:
                    sellers += str(tiendas_raw[i])
                else:
                    sellers += str(tiendas_raw[i]) + "_"
            print(sellers)
            return graph_implementation.get_brands_sellers(sellers)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})


'''
@app.get("/sellers", tags=["Other"])
def get_sellers() -> JSONResponse:
    try:
        mySet = SetSeller()
        return mySet.sellers_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

#Set by seller
@app.get("/products/filter/seller", tags=["Set"])
def get_products_seller(seller:str) -> JSONResponse:
    try:
        mySet = SetSeller()
        return mySet.products_seller_json(seller)
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: No hay tienda {e}"})
'''