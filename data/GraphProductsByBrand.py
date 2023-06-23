
import pandas as pd
from data.Product import Product
from data.Graph import Graph


class GraphProductsByBrand:

    def __init__(self, filePath) -> None:
        #Leer productos
        self.lector = pd.read_csv(f'{filePath}')
        #Implementación
        self.graph = Graph()
        self.insert_products()

    def insert_products(self) -> None:
        brands_inserted = []

        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i], seller=self.lector['marca'][i], image=self.lector['imagen'][i], brand=self.lector['empresa'][i])
            cur_brand = self.lector['empresa'][i]

            self.graph.add_vertex(curProduct)
            if not (cur_brand in brands_inserted):
                self.graph.add_vertex(cur_brand)
                brands_inserted.append(cur_brand)

            self.graph.add_edge(curProduct, cur_brand)

        self.brands = brands_inserted

    def get_products(self, brands:str) -> list:
        brands_list:list = brands.split('_')
        products_asked:list = []

        for brand in brands_list:
            products = self.graph.get_neighbors(brand)
            for product in products:
                products_asked.append(product.json())

        return products_asked
    
    def get_brands(self) -> list:
        return {"marcas":self.brands}

def graph_brand_implementation() -> GraphProductsByBrand:
    return GraphProductsByBrand("src\productos.csv")