from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #enviarle datos al servidor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm



PATH = "/Users/knsmolina.28/Downloads/chromedriver_mac64/chromedriver"
driver  = webdriver.Chrome(PATH)
driver.get("https://www.mercadolibre.com.co/")

print(driver.title)
search_bar = driver.find_element(by=By.CLASS_NAME, value="nav-search-input")
search_bar.clear()
busqueda = ["Televisor Samsung", "Iphone 11", "Samsung a53","Xiaomi redmi note 8"]

longitud = len( busqueda )
#data_product = {"titulo":[],"precio":[],"link":[]}
data_product = {"precio":[]}

for i in tqdm(range(longitud)):
    search_bar = driver.find_element(by = By.CLASS_NAME, value="nav-search-input")
    search_bar.clear()
    search_bar.send_keys(busqueda[i])
    search_bar.send_keys(Keys.RETURN)

    title_products = driver.find_elements(by=By.XPATH, value="//h2[@class='ui-search-item__title shops__item-title']")
    title_products = [title.text for title in title_products]
    price_products = driver.find_elements(by=By.XPATH, value="//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-amount']//span[2]")
    price_products = [price.text for price in price_products]

    links_products = driver.find_elements(by=By.XPATH, value="//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]")
    links_products = [link.get_attribute("href") for link in links_products]
    print(links_products)
    print(price_products)
    print(title_products)

     #diccionario
    #data_product["titulo"].extend(title_products)
    data_product["precio"].extend(price_products)
    #data_product["link"].extend(title_products)



df = pd.DataFrame(data_product)
df.to_csv("productos.csv")

#print(price_products)
#print(title_products)


time.sleep(4)
driver.close()

#//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left"]/div[1]/div//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag-amount"]//span[2]

#//div[@=class="ui-search-item__group ui-search-item__group--title shops__items-group"]//a[1]


