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
from data.UserCmpListHash import UserCmpListHash
from data.ComparisonListAVL2 import ComparisonListAVL2
from data.ComparisonListHash import ComparisonListHash

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

def validate_session() -> bool:
    if user_active["active"] != None:
        return True
    else:
        raise Exception("La sesión no está activa")

#Users

@app.get("/user/", tags=["User"])
async def validate_user(cur_email:str, cur_password:str) -> JSONResponse:
    try:
        cur_user = User(email=cur_email, password=cur_password, operation=1)
        user_active["active"] = cur_user
        return {"message" : f"Se ha iniciado la sesión con éxito para el usuario {cur_email}"}
    except Exception as e:
        return {"message" : str(e)}
    
@app.get("/user/session", tags=["User"])
async def session_user() -> JSONResponse:
    try:
        if user_active["active"]:
            return user_active["active"].json()
        else:
            return {"message" : "No se ha iniciado sesión"}    
    except Exception as e:
        return {"message" : str(e)}
    
@app.put("/user/log_out", tags=["User"])
async def log_out_user() -> JSONResponse:
    if user_active["active"]:
        user_active["active"] = None
        return {"mesage" : "Se ha cerrado la sesión"} 
    else:
        return {"mesage" : "No hay sesión iniciada"} 
    
@app.post("/user/", tags=["User"])
async def create_user(email:str, password:str, nombre:str, apellido:str) -> JSONResponse:
    try:
        cur_user = User(email=email, password=password, operation=2, name=nombre, last_name=apellido)
        user_active["active"] = cur_user
        return JSONResponse(content={f"message":f"Usuario creado con email {cur_user.email} y sesión iniciada"})
    except Exception as e:
        return {"message" : str(e)}
    
@app.put("/user/", tags=["User"])
async def modify_user(nombre:str=None, apellido:str=None, email:str=None, password:str=None) -> JSONResponse:
    try:
        if validate_session():
            cur_user:User = user_active["active"]
            cur_user.update(name=nombre, last_name=apellido, email=email, password=password)
            return JSONResponse(content={f"message":f"Usuario con email {cur_user.email} actualizado"})
    except Exception as e:
        return {"message" : str(e)}
    
@app.delete("/user/", tags=["User"])
async def delete_user() -> JSONResponse:
    try:
        if validate_session():
            cur_user:User = user_active["active"]
            cur_user.delete()
            user_active["active"] = None
            return {"message": f"Usuario con email {cur_user.email} eliminado exitosamente"}
    except Exception as e:
        return {"message" : str(e)}


#Results

@app.get("/product/", tags=["Products"])
def get_products_key(keyProd:str) -> JSONResponse:
    Search.Search(str(keyProd))
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    return resulAVL_imp.view_results()
    '''
    try:
        Search.Search(str(keyProd))
        resulAVL_imp = ResultsAVL.results_AVL_imp()
        return resulAVL_imp.view_results()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    '''

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

def validate_user_has_wish_list(wish_list_id) -> bool:
    flag = False

    cur_user:User = user_active["active"]

    if cur_user != None:
        user_wishList_hash = UserWListHash()
        user_wish_lists = user_wishList_hash.wish_lists_by_user(cur_user.id)
        if wish_list_id in user_wish_lists:
            return True
        else:
            raise Exception(f"El usuario no tiene la wish list {wish_list_id}")
    else:
        raise Exception("No ha iniciado sesión")
    
    return flag

@app.get("/wish_list/", tags=["Wish List"])
def show_wish_list_by_id(id:int) -> JSONResponse:
    try:
        if validate_user_has_wish_list(id):
            wish_lists_imp = WishListHeap(id)
            return wish_lists_imp.view_whish_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.post("/wish_list/product", tags=["Wish List"])
def new_in_wish_list(wish_list_id:int, titulo:str, precio:int, link:str, tienda:str, imagen:str, marca:str) -> JSONResponse:
    try:
        if validate_user_has_wish_list(wish_list_id):
            whishListHeap_imp = WishListHeap(wish_list_id)
            cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
            whishListHeap_imp.insert(cur_product)
            return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title} en la lista {wish_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {titulo} ya que {e}"})

@app.delete("/wish_list/product", tags=["Wish List"])
def delete_in_wish_list(wish_list_id:int, titulo:str, precio:int, link:str, tienda:str, imagen:str, marca:str) -> JSONResponse:
    try:
        if validate_user_has_wish_list(wish_list_id):
            wishListHeap_imp = WishListHeap(wish_list_id)
            cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
            wishListHeap_imp.delete(cur_product)
            return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title} en la lista {wish_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto: {titulo} ya que no existe y/o {e}"})
    
@app.delete("/wish_list/max_product", tags=["Wish List"])
def delete_max_in_wish_List(wish_list_id:int) -> JSONResponse:
    try:
        if validate_user_has_wish_list(wish_list_id):
            wishListHeap_imp = WishListHeap(wish_list_id)
            prod_del = wishListHeap_imp.delete_max()
            return JSONResponse(content={"message":f"Se eliminó el producto: {prod_del.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"No se eliminó el producto con menor precio ya que {e}"})
    

#List of Wish Lists

@app.post("/wish_list/", tags=["Wish List"])
def post_wish_list(name:str=None) -> JSONResponse:
    try:
        if validate_session():

            cur_user:User = user_active["active"]

            user_wishlist = UserWListHash()
            user_has_wish_lists =  user_wishlist.data_hash_table.find(cur_user.id)

            if user_has_wish_lists:
                wish_list_ids:list = user_wishlist.wish_lists_by_user(cur_user.id)
            else:
                wish_list_ids = []
                

            wish_lists_hashTable = WishListsHash()
            wish_list_id = wish_lists_hashTable.create(name, [], wish_list_ids)

            cur_user:User = user_active["active"]

            user_wishList = UserWListHash()
            user_wishList.insert(cur_user.id, wish_list_id)
            return JSONResponse(content={"message":f"Lista creada exitosamente con ID: {wish_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

@app.get("/wish_list/id", tags=["Wish List"])
def wish_list_by_name(name:str) -> JSONResponse:
    try:
        if validate_session():
            wish_lists_hashTable = WishListsHash()
            wish_list_ids:list = wish_lists_hashTable.find_id(name)
            wish_list_id = None

            for id in wish_list_ids:
                try:
                   flag = validate_user_has_wish_list(id) 
                except Exception:
                    flag = False
                if flag:
                    wish_list_id = id
                    break
            
            if wish_list_id == None:
                raise Exception(f"El usuario no tiene una lista de deseos guardada como {name}")

            return JSONResponse(content={"message":wish_list_id})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/wish_list/name", tags=["Wish List"])
def wish_list_by_id(id:int) -> JSONResponse:
    try:
        if validate_user_has_wish_list(id):
            wish_lists_hashTable = WishListsHash()
            wish_list_name = wish_lists_hashTable.find_name(str(id))
            return JSONResponse(content={"message":wish_list_name})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.get("/wish_list/ids", tags=["Wish List"])
def all_wish_list_by_user() -> JSONResponse:
    try:
        if validate_session():
            cur_user:User = user_active["active"]

            user_wishlist = UserWListHash()
            wish_list_ids:list = user_wishlist.wish_lists_by_user(cur_user.id)

            return JSONResponse(content={"message":wish_list_ids})
    
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.put("/wish_list/name", tags=["Wish List"])
def update_wish_list_name(id:int, new_name:str) -> JSONResponse:
    try:
        if validate_user_has_wish_list(id):

            cur_user:User = user_active["active"]

            user_wishlist = UserWListHash()
            wish_list_ids:list = user_wishlist.wish_lists_by_user(cur_user.id)

            wish_lists_hashTable = WishListsHash()
            wish_list_name = wish_lists_hashTable.update_name(id, new_name, wish_list_ids)
            return JSONResponse(content={"message":f"Nombre actualizado exitosamente a {new_name}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
@app.delete("/wish_list/", tags=["Wish List"])
def delete_wish_list_by_id(id:int) -> JSONResponse:
    try:
        if validate_user_has_wish_list(id):
            wish_lists_hashTable = WishListsHash()
            wish_lists_hashTable.delete_wish_list(id)

            user_wishList = UserWListHash()
            cur_user:User = user_active["active"]
            user_wishList.delete_wish_list(cur_user.id, id)

            return JSONResponse(content={"message":f"Wish list con id {id} eliminada con exito"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})

'''
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
'''

#Comparison List2
def validate_user_has_comparison_list(comparison_list_id) -> bool:
    flag = False

    cur_user:User = user_active["active"]

    if cur_user != None:
        user_comparisonList_hash = UserCmpListHash()
        user_comparison_lists = user_comparisonList_hash.comparison_lists_by_user(cur_user.id)
        if comparison_list_id in user_comparison_lists:
            return True
        else:
            raise Exception(f"El usuario no tiene la comparison list {comparison_list_id}")
    else:
        raise Exception("No ha iniciado sesión")
    
    return flag

@app.get("/comparison_list2/", tags=["Comparison List2"])
def show_comparison_list(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            return comparison.view_comparison_list_json()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    

@app.get("/comparison_list2/order/", tags=["Comparison List2"])
def show_ComparisonList_order(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            return comparison.inOrder_JSON()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    

@app.get("/comparison_list2/order_inverted/", tags=["Comparison List2"])
def show_ComparisonList_order_inverted(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            return comparison.inOrderInv_JSON()
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    


@app.get("/comparison_list2/comparison/", tags=["Comparison List2"])
def show_ComparisonList_comparison(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            return_best_worst:list = []
            return_best_worst.append(comparison.compareByPrice_json()[0]["best"])
            return_best_worst.append(comparison.compareByPrice_json()[0]["worst"])

            return return_best_worst
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})


@app.post("/comparison_list2/product", tags=["Comparison List2"])
def new_in_comparison_list(id_comparison:int, titulo:str, precio:int, link:str, tienda:str, imagen:str, marca:str) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
            comparison.insert(cur_product)
            return JSONResponse(content={"message":f"Se registró el producto: {cur_product.title}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error al ingresar el producto: {titulo} ya que {e}"})


@app.delete("/comparison_list2/product", tags=["Comparison List2"])
def delete_in_comparison_list(id_comparison:int, titulo:str, precio:int, link:str, tienda:str, imagen:str, marca:str) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison = ComparisonListAVL2(id_comparison)
            cur_product = Product(title=titulo, price=precio, link=link, seller=tienda, image=imagen, brand=marca)
            comparison.delete(cur_product)
            return JSONResponse(content={"message":f"Se eliminó el producto: {cur_product.title}"})
    except Exception as e:
        print(e)
        return JSONResponse(content={f"message":f"No se eliminó el producto: {titulo} ya que no existe y/o {e}"})

#List of comparison lists

@app.post("/comparison_list2/", tags=["Comparison List2"])
def post_comparison_list(name:str=None) -> JSONResponse:
    try:
        if validate_session():

            cur_user:User = user_active["active"]

            user_comparisonlist = UserCmpListHash()
            user_has_comparisonlist = user_comparisonlist.data_hash_table.find(cur_user.id)

            if user_has_comparisonlist:
                comparison_list_ids:list = user_comparisonlist.comparison_lists_by_user(cur_user.id)
            else:
                comparison_list_ids = []
        
            comparison_lists_hashTable = ComparisonListHash()
            comparison_list_id = comparison_lists_hashTable.create(name, [], comparison_list_ids)

            cur_user:User = user_active["active"]

            user_comparisonList = UserCmpListHash()
            user_comparisonList.insert(cur_user.id, comparison_list_id)
            return JSONResponse(content={"message":f"Lista creada exitosamente con ID: {comparison_list_id}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    

@app.get("/comparison_list2/id", tags=["Comparison List2"])
def comparison_list_by_name(name:str) -> JSONResponse:
    try:
        if validate_session():
            comparison_lists_hashTable = ComparisonListHash()
            comparison_list_ids:list = comparison_lists_hashTable.find_id(name)
            comparison_list_id = None

            for id in comparison_list_ids:
                try:
                   flag = validate_user_has_comparison_list(id) 
                except Exception:
                    flag = False
                if flag:
                    comparison_list_id = id
                    break
            
            if comparison_list_id == None:
                raise Exception(f"El usuario no tiene una comparison list guardada como {name}")

            return JSONResponse(content={"message":comparison_list_id})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
    
@app.get("/comparison_list2/name", tags=["Comparison List2"])
def comparison_list_by_id(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison_lists_hashTable = ComparisonListHash()
            comparison_list_name = comparison_lists_hashTable.find_name(str(id_comparison))
            return JSONResponse(content={"message":comparison_list_name})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
    
@app.get("/comparison_list2/ids", tags=["Comparison List2"])
def all_comparison_list_by_user() -> JSONResponse:
    try:
        if validate_session():
            cur_user:User = user_active["active"]

            user_comparisonlist = UserCmpListHash()
            comparison_list_ids:list = user_comparisonlist.comparison_lists_by_user(cur_user.id)

            return JSONResponse(content={"message":comparison_list_ids})
    
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
    
@app.put("/comparison_list2/name", tags=["Comparison List2"])
def update_comparison_list_name(id_comparison:int, new_name:str) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):

            cur_user:User = user_active["active"]

            user_comparisonlist = UserCmpListHash()
            comparison_list_ids:list = user_comparisonlist.comparison_lists_by_user(cur_user.id)

            comparison_lists_hashTable = ComparisonListHash()
            comparison_list_name = comparison_lists_hashTable.update_name(id_comparison, new_name, comparison_list_ids)
            return JSONResponse(content={"message":f"Nombre actualizado exitosamente a {new_name}"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    
    
@app.delete("/comparison_list2/", tags=["Comparison List2"])
def delete_comparison_list_by_id(id_comparison:int) -> JSONResponse:
    try:
        if validate_user_has_comparison_list(id_comparison):
            comparison_lists_hashTable = ComparisonListHash()
            comparison_lists_hashTable.delete_comparison_list(id_comparison)

            user_comparisonList = UserCmpListHash()
            cur_user:User = user_active["active"]
            user_comparisonList.delete_comparison_list(cur_user.id, id_comparison)

            return JSONResponse(content={"message":f"Wish list con id {id_comparison} eliminada con exito"})
    except Exception as e:
        return JSONResponse(content={f"message":f"Error: {e}"})
    

#Other

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
    graph_implementation = GraphProducts.graph_implementation()
    if not sellers is None:
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
    '''
    try:
        graph_implementation = GraphProducts.graph_implementation()
        if not sellers is None:
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