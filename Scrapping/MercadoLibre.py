from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm

def searchProduct(keyWord, data_product:dict, driver:webdriver.Chrome) -> dict:

    driver.get("https://www.mercadolibre.com.co/")

    print(driver.title)
    search_bar = driver.find_element(by=By.CLASS_NAME, value="nav-search-input")
    search_bar.clear()
    busqueda = [f"{keyWord}"]

    search_bar = driver.find_element(by=By.CLASS_NAME, value="nav-search-input")
    search_bar.clear()
    search_bar.send_keys(busqueda)
    search_bar.send_keys(Keys.RETURN)

    title_products = driver.find_elements(by=By.XPATH, value="//h2[@class='ui-search-item__title shops__item-title']")
    title_products = [title.text for title in title_products]

    price_products = driver.find_elements(by=By.XPATH, value="//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-amount']//span[2]")
    price_products = [int(price.text.replace("$", "").replace(".", "")) for price in price_products]

    links_products = driver.find_elements(by=By.XPATH, value="//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]")
    links_products = [link.get_attribute("href") for link in links_products]

    image_products = driver.find_elements(by=By.XPATH, value="//img[contains(@class, 'ui-search-result-image__element') and contains(@class, 'shops__image-element')]")
    image_urls = [image.get_attribute("data-src") for image in image_products]

    marcas = ['Xiaomi', 'Sony', 'Kalley', 'Braun', 'Maytag', 'Realme', 'Alcatel', 'Challenger', 'Alexa', 'Babyliss',
              'Honor', 'TCL', 'LG', 'Nokia', 'Huawei', 'Haceb', 'Panasonic', 'Lenovo', 'Whirlpool', 'MSI', 'Gama',
              'Zte', 'Conair', 'Remington', 'Samsung', 'Oppo', 'Mabe', 'Canon', 'Asus', 'Electrolux', 'iPhone', 'GE',
              'Philips', 'Acer', 'Acros', 'vivo', 'ROG', 'Motorola', 'Wahl', 'Fujifilm', 'GoPro', 'Google Home', 'HP',
              'Tecno', 'Legion', 'Moto', 'Apple', 'Nintendo', 'Microsoft', 'Sony']


    marcas_productos = []
    for title in title_products:
        marca_encontrada = False
        for marca in marcas:
            if marca.lower() in title.lower():
                marcas_productos.append(marca)
                marca_encontrada = True
                break
        if not marca_encontrada:
            marcas_productos.append("Otra")

    brand_products = ["Mercado Libre" for _ in range(len(links_products))]

    print(title_products)
    print(price_products)
    print(links_products)
    print(brand_products)
    print(image_urls)
    print(marcas_productos)

    # Extender las listas en el diccionario "data_product"
    data_product["titulo"].extend(title_products)
    data_product["precio"].extend(price_products)
    data_product["link"].extend(links_products)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(image_urls)
    data_product["empresa"].extend(marcas_productos)

    time.sleep(4)
    driver.close()

    return data_product
