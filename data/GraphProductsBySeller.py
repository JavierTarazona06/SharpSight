
import pandas as pd
from data.Product import Product
from data.Graph import Graph


class GraphProductsBySeller:

    def __init__(self, filePath) -> None:
        #Leer productos
        self.lector = pd.read_csv(f'{filePath}')
        #Implementación
        self.graph = Graph()
        self.insert_products()

    def insert_products(self) -> None:
        sellers_inserted = []

        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i], seller=self.lector['marca'][i], image=self.lector['imagen'][i], brand=self.lector['empresa'][i])
            cur_seller = self.lector['marca'][i]

            self.graph.add_vertex(curProduct)
            if not (cur_seller in sellers_inserted):
                self.graph.add_vertex(cur_seller)
                sellers_inserted.append(cur_seller)

            self.graph.add_edge(curProduct, cur_seller)


    def get_products(self, sellers:str) -> list:
        sellers_list:list = sellers.split('_')
        products_asked:list = []

        for seller in sellers_list:
            products = self.graph.get_neighbors(seller)
            for product in products:
                products_asked.append(product.json())

        return products_asked

def graph_seller_implementation() -> GraphProductsBySeller:
    return GraphProductsBySeller("src\productos.csv")     
