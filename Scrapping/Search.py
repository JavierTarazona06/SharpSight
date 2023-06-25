import copy
import pandas as pd

from Scrapping import Exito, Ktronix, MercadoLibre, Amazon, Linio

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from data.HashTable import HashTable

class Search:

    def __init__(self, product_to_search):

        data_product = {"titulo": [], "precio": [], "link": [], "marca":[], "imagen":[], "empresa":[]}

        #driver : webdriver.Chrome = self.reload_driver()
        #data_product = MercadoLibre.searchProduct(product_to_search, data_product, driver)
 
        #driver : webdriver.Chrome = self.reload_driver()
        #data_product = Ktronix.searchProduct(product_to_search, data_product, driver)

        #driver : webdriver.Chrome = self.reload_driver()
        #data_product = Exito.searchProduct(product_to_search, data_product, driver)

        driver : webdriver.Chrome = self.reload_driver()
        data_product = Linio.searchProduct(product_to_search, data_product, driver)

        #driver : webdriver.Chrome = self.reload_driver()
        #data_product = Amazon.searchProduct(product_to_search, data_product, driver)

        print(len(data_product.get("titulo")))
        print(len(data_product.get("precio")))
        print(len(data_product.get("link")))
        print(len(data_product.get("marca")))
        print(len(data_product.get("imagen")))
        print(len(data_product.get("empresa")))

        #Integridad de los titulos
        hash = HashTable()

        titulos = copy.deepcopy(data_product.get("titulo"))
        acc = 0
        for product_title in titulos:
            find_positions = hash.rabin_karp(str(product_title).lower(), str(product_to_search).lower())
            if len(find_positions) == 0:
                data_product.get("titulo").pop(acc)
                data_product.get("precio").pop(acc)
                data_product.get("link").pop(acc)
                data_product.get("marca").pop(acc)
                data_product.get("imagen").pop(acc)
                data_product.get("empresa").pop(acc)
                acc -= 1
            acc += 1

        print("R-K")
        print(len(data_product.get("titulo")))
        print(len(data_product.get("precio")))
        print(len(data_product.get("link")))
        print(len(data_product.get("marca")))
        print(len(data_product.get("imagen")))
        print(len(data_product.get("empresa")))

        if len(data_product.get("titulo")) == 0:
            raise Exception("La búsqueda no arrojó resultados. Intenta una búsqueda más general o verifica la ortografía")

        df = pd.DataFrame(data_product)
        df.to_csv("src/productos.csv")

    def reload_driver(self, headless=True) -> webdriver.Chrome:

        PATH = "chromedriver"

        if headless:
            # Ejecutar en modo headless sin ventana visible
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(PATH, options=chrome_options)
        else:
            #Ventana Visible
            driver = webdriver.Chrome(PATH)
                
 

        return driver