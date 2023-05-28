from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #enviarle datos al servidor
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


    search_bar = driver.find_element(by = By.CLASS_NAME, value="nav-search-input")
    search_bar.clear()
    search_bar.send_keys(busqueda)
    search_bar.send_keys(Keys.RETURN)

    title_products = driver.find_elements(by=By.XPATH, value="//h2[@class='ui-search-item__title shops__item-title']")
    title_products = [title.text for title in title_products]
    price_products = driver.find_elements(by=By.XPATH, value="//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-amount']//span[2]")
    price_products = [int(price.text.replace("$", "").replace(".", "")) for price in price_products]

    links_products = driver.find_elements(by=By.XPATH, value="//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]")
    links_products = [link.get_attribute("href") for link in links_products]

    brand_products = ["Mercado Libre" for i in range(len(links_products))]

    print(title_products)
    print(price_products)
    print(links_products)
    print(brand_products)

    #diccionario
    data_product["titulo"].extend(title_products)
    data_product["precio"].extend(price_products)
    data_product["link"].extend(links_products)
    data_product["marca"].extend(brand_products)

    time.sleep(4)
    driver.close()

    return data_product
