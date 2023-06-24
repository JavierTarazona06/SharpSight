
import pandas as pd
from data.Product import Product
from data.Graph import Graph


class GraphProducts:

    def __init__(self, filePath) -> None:
        #Leer productos
        self.lector = pd.read_csv(f'{filePath}')
        #Implementación
        self.graph = Graph()
        self.insert_products()

    def insert_products(self) -> None:
        brands_inserted = []
        sellers_inserted = []

        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i], seller=self.lector['marca'][i], image=self.lector['imagen'][i], brand=self.lector['empresa'][i])
            cur_brand = self.lector['empresa'][i]
            cur_seller = self.lector['marca'][i]

            self.graph.add_vertex(curProduct)

            if not (cur_brand in brands_inserted):
                self.graph.add_vertex(cur_brand)
                brands_inserted.append(cur_brand)

            if not (cur_seller in sellers_inserted):
                self.graph.add_vertex(cur_seller)
                sellers_inserted.append(cur_seller)

            self.graph.add_edge(curProduct, cur_brand)
            self.graph.add_edge(curProduct, cur_seller)
            self.graph.add_edge(cur_brand, cur_seller)

        self.brands = brands_inserted
        self.sellers = sellers_inserted

    def get_products_brand(self, brands:str) -> list:
        brands_list:list = brands.split('_')
        products_asked:list = []

        for brand in brands_list:
            products = self.graph.get_neighbors(brand)
            for product in products:
                if str(type(product)) == "<class 'data.Product.Product'>":
                    products_asked.append(product.json())

        return products_asked
    
    def get_products_seller(self, sellers:str) -> list:
        sellers_list:list = sellers.split('_')
        products_asked:list = []

        for seller in sellers_list:
            products = self.graph.get_neighbors(seller)
            for product in products:
                if str(type(product)) == "<class 'data.Product.Product'>":
                    products_asked.append(product.json())

        return products_asked
    
    def get_brands(self) -> dict:
        return {"marcas":self.brands}
    
    def get_sellers(self) -> dict:
        return {"tiendas":self.sellers}
    
    def get_brands_sellers(self, sellers:str) -> dict:
        sellers_list:list = sellers.split('_')
        brands_asked:list = []
        to_return = {}

        for seller in sellers_list:
            brands = self.graph.get_neighbors(seller)
            for brand in brands:
                if str(type(brand)) == "<class 'str'>":
                    brands_asked.append(brand)
            to_return[str(seller)] = brands_asked
            brands_asked = []

        return to_return


def graph_implementation() -> GraphProducts:
    return GraphProducts("src\productos.csv")