import csv
import os
import pandas as pd
from data.ComparisonListHash import ComparisonListHash

from data.AVL import AVL
from data.NodeT import NodeT
from data.Product import Product


class ComparisonListAVL2:

    def __init__(self, comparison_list_id) -> None:

        self.data_path = "src/comparisonList.csv"
        
        comparison_lists_hashTable = ComparisonListHash()

        if not comparison_lists_hashTable.find(comparison_list_id):
            raise Exception(f"Error: No existe la lista con id {comparison_list_id}")
        else:
            data:dict = comparison_lists_hashTable.data_hash_table.get(comparison_list_id)
            #data = {id: 'name', 'content'}
            comparison_list_name = data["name"]
            comparison_list_content = data["content"]

            self.tree_data = AVL()
            self.indices_csv :dict = {}
            self.id = comparison_list_id
            self.name = comparison_list_name
            
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
            for product_json in comparison_list_content:
                curProd = Product(product_json["titulo"], product_json["precio"], product_json["link"], product_json["tienda"], product_json["imagen"], product_json["marca"])
                self.insert(curProd)
                self.indices_csv[str(curProd)] = i
                i += 1

    def __str__(self):
        return str(self.tree_data.preOrder())
    
    def save_data_list_cp(self, nombre=None):
        list_cp_hashTable = ComparisonListHash()
        if self.id==None:
            raise Exception("No se ha creado la lista de comparación")
        list_cp_hashTable.set(comparison_list_id=self.id, name=nombre, comparison_list_content=self.view_comparison_list_json())
    
    def insert(self, prod: Product):
        self.tree_data.insert(prod)
        df = pd.read_csv("src/comparisonList.csv")
        rows = df.shape[0]
        self.indices_csv[str(prod)] = len(df)
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link, "seller":prod.seller, "image":prod.image, "brand": prod.brand}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/comparisonList.csv", index=False)

        self.save_data_list_cp()

    def delete(self, product:Product):
        self.tree_data.delete(NodeT(product))
        index_csv = self.indices_csv[str(product)]

        df = pd.read_csv("src/comparisonList.csv")
        
        if index_csv == 0:
            df = df.iloc[1:]
        elif index_csv == (len(df)-1):
            df = df.iloc[0:index_csv]
        else:
            df = pd.concat([df.iloc[0:index_csv], df.iloc[index_csv+1:]]) #Elimina la fila del indice

        df.to_csv("src/comparisonList.csv", index=False)
        print("Deleted from comparison list: " + str(product))

        self.save_data_list_cp()

    def orderListPrice(self) -> str:
        return self.tree_data.inOrder()

    def orderListPriceReverse(self) -> str:
        return self.tree_data.inOrderInv()
    
    def preOrderCall_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result.append(ptr.key.json())
            result = self.preOrderCall_JSON(ptr.left,result)
            result = self.preOrderCall_JSON(ptr.right, result)
            return result

    def preOrder_JSON(self) -> list:
        result = []
        return self.preOrderCall_JSON(self.tree_data.root, result)
    
    def view_comparison_list_json(self) -> list:
        return self.preOrder_JSON()
    
    def inOrderCall_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result = self.inOrderCall_JSON(ptr.left, result)
            result.append(ptr.key.json())
            result = self.inOrderCall_JSON(ptr.right, result)
            return result

    def inOrder_JSON(self) -> list:
        result = []
        return self.inOrderCall_JSON(self.tree_data.root, result)
    
    def view_list_order_json(self) -> list:
        return self.inOrder_JSON()
    
    def inOrderCallInv_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result = self.inOrderCallInv_JSON(ptr.right, result)
            result.append(ptr.key.json())
            result = self.inOrderCallInv_JSON(ptr.left, result)
            return result

    def inOrderInv_JSON(self) -> list:
        result = []
        return self.inOrderCallInv_JSON(self.tree_data.root, result)
    
    def view_list_orderInv_json(self) -> list:
        return self.inOrderInv_JSON()
    
    def compareByPrice(self):
        best : Product = self.tree_data.min().key
        worst : Product = self.tree_data.max().key
        returning = "According to price...\n"
        returning += "  The best product is: "+str(best)+"\n"
        returning += "  The most expensive product is: " + str(worst) + "\n"
        returning += "--Presenting all the results:\n"
        returning += str(self.tree_data.inOrder())
        return returning
    
    def compareByPrice_json(self) -> list:
        returning = []
        data_dict :dict = {}
        best : Product = self.tree_data.min().key
        worst : Product = self.tree_data.max().key
        data_dict["best"] = best.json()
        data_dict["worst"] = worst.json()
        data_dict["products_order"] = self.view_list_order_json()
        returning.append(data_dict)
        return returning