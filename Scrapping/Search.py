import pandas as pd

from Scrapping import Exito, Ktronix, MercadoLibre

class Search:

    def __init__(self, product_to_search):

        data_product = {"titulo": [], "precio": [], "link": [], "marca":[]}

        data_product = MercadoLibre.searchProduct(product_to_search, data_product)
        data_product = Ktronix.searchProduct(product_to_search, data_product)
        data_product = Exito.searchProduct(product_to_search, data_product)


        df = pd.DataFrame(data_product)
        df.to_csv("src/productos.csv")