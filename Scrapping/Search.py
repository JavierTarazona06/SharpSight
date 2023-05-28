import pandas as pd

from Scrapping import Exito, Ktronix, MercadoLibre

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Search:

    def __init__(self, product_to_search):

        data_product = {"titulo": [], "precio": [], "link": [], "marca":[], "imagen":[], "empresa":[]}

        driver : webdriver.Chrome = self.reload_driver()

        data_product = MercadoLibre.searchProduct(product_to_search, data_product, driver)
 
        driver : webdriver.Chrome = self.reload_driver()
 
        data_product = Ktronix.searchProduct(product_to_search, data_product, driver)

        driver : webdriver.Chrome = self.reload_driver()

        data_product = Exito.searchProduct(product_to_search, data_product, driver)


        df = pd.DataFrame(data_product)
        df.to_csv("src/productos.csv")

    def reload_driver(self) -> webdriver.Chrome:
        
        # Ejecutar en modo headless sin ventana visible
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        PATH = "chromedriver"
        #Visible
        #driver = webdriver.Chrome(PATH)
        #No visible
        driver = webdriver.Chrome(PATH, options=chrome_options)

        return driver