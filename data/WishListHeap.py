import json
from data.HeapMax import HeapMax
import pandas as pd
import os
import csv
from data.Product import Product
from data.WishListsHash import WishListsHash

class WishListHeap:

    def __init__(self, wish_list_id:int) -> None:

        self.data_path = "src/wishList.csv"
        
        wish_lists_hashTable = WishListsHash()

        if not wish_lists_hashTable.find(wish_list_id):
            raise Exception(f"Error: No existe la lista con id {wish_list_id}")
        else:
            data:dict = wish_lists_hashTable.data_hash_table.get(wish_list_id)
            #data = {id: 'name', 'content'}
            wish_list_name = data["name"]
            wish_list_content = data["content"]

            self.list = HeapMax()
            self.indices_csv :dict = {}

            self.id = wish_list_id
            self.name = wish_list_name
            
            if not os.path.exists(self.data_path):
                with open(self.data_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['title', 'price', 'link','seller','image','brand'])
            else:
                with open(self.data_path, 'w', newline='') as data:
                    data.truncate()
                with open(self.data_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['title', 'price', 'link','seller','image','brand'])

            i = 0
            for product_json in wish_list_content:
                curProd = Product(product_json["titulo"], product_json["precio"], product_json["link"], product_json["tienda"], product_json["imagen"], product_json["marca"], )
                print(curProd)
                self.insert(curProd)
                self.indices_csv[str(curProd)] = i
                i += 1
        '''
        self.list = HeapMax()
        self.indices_csv :dict = {}
        self.data_path = "src/wishList.csv"
        if os.path.exists(self.data_path):
            self.lector = pd.read_csv("src/wishList.csv")
            row_count = len(self.lector)
            for i in range(row_count):
                curProduct : Product = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                 link=self.lector['link'][i], seller=self.lector['seller'][i], image=self.lector['image'][i], brand=self.lector['brand'][i])
                self.list.insert(curProduct)
                self.indices_csv[str(curProduct)] = i
        else:
            with open("src/wishList.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'price', 'link','seller','image','brand'])
        '''

    def load_data(self, wish_list_id) -> list:

        wish_lists_hashTable = WishListsHash()

        if not wish_lists_hashTable.find(wish_list_id):
            raise Exception(f"Error: No existe la lista con id {wish_list_id}")
        else:
            data:dict = wish_lists_hashTable.data_hash_table.get(wish_list_id)
            #data = {id: 'name', 'content'}
            wish_list_name = data["name"]
            wish_list_content = data["content"]

            self.list = HeapMax()
            self.indices_csv :dict = {}

            self.id = wish_list_id
            self.name = wish_list_name
            
            if not os.path.exists(self.data_path):
                with open(self.data_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['title', 'price', 'link','seller','image','brand'])
            else:
                with open(self.data_path, 'w', newline='') as data:
                    data.truncate()
                with open(self.data_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['title', 'price', 'link','seller','image','brand'])

            i = 0
            for product_json in wish_list_content:
                curProd = Product(product_json["titulo"], product_json["precio"], product_json["link"], product_json["tienda"], product_json["imagen"], product_json["marca"], )
                print(curProd)
                self.insert(curProd)
                self.indices_csv[str(curProd)] = i
                i += 1

            return wish_list_content

    def save_data_list_wl(self, nombre=None):
        list_wl_hashTable = WishListsHash()
        if not self.id:
            raise Exception("No se ha creado la lista de desos")
        list_wl_hashTable.set(wish_list_id=self.id, name=nombre, wish_list_content=self.view_whish_list_json())

    def __str__(self):
        return str(self.list.array)
    
    def view_whish_list_json(self):
        return self.list.array.json()
    
    def insert(self, prod: Product):
        if (self.list.array.empty()) or (not self.list.array.find(prod)):
            self.list.insert(prod)
            df = pd.read_csv("src/wishList.csv")
            rows = df.shape[0]
            self.indices_csv[str(prod)] = len(df)
            data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link, "seller":prod.seller, "image":prod.image, "brand": prod.brand}, index=[rows])
            df = pd.concat([df, data])
            df.to_csv("src/wishList.csv", index=False)

            self.save_data_list_wl()
        else:
            raise Exception("Produco ya existe")

    def delete_max(self) -> Product:
        prod : Product = self.list.get_max()
        index_prod = self.indices_csv[str(prod)]
        prod : Product = self.list.extract_max()
        df = pd.read_csv("src/wishList.csv")

        if index_prod == 0:
            df = df.iloc[1:]
        elif index_prod == (len(df)-1):
            df = df.iloc[0:index_prod]
        else:
            df = pd.concat([df.iloc[0:index_prod], df.iloc[index_prod+1:]]) #Elimina la fila del indice
        df.to_csv("src/wishList.csv", index=False)
        print("Deleted from wish list: "+str(prod))

        self.save_data_list_wl()
        return prod

    
    def delete(self, prod:Product):
        index_list = self.list.array.findPosition(prod)
        index_csv = self.indices_csv[str(prod)]
        self.list.remove_product(index_list)

        df = pd.read_csv("src/wishList.csv")

        if index_csv == 0:
            df = df.iloc[1:]
        elif index_csv == (len(df)-1):
            df = df.iloc[0:index_csv]
        else:
            df = pd.concat([df.iloc[0:index_csv], df.iloc[index_csv+1:]]) #Elimina la fila del indice
        df.to_csv("src/wishList.csv", index=False)
        print("Deleted from wish list: "+str(prod))

        self.save_data_list_wl()