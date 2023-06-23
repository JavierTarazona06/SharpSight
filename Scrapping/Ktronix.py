from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from tqdm import tqdm

def searchProduct(keyWord, data_product : dict, driver: webdriver.Chrome) -> dict:

    driver.get("https://www.ktronix.com/")

    print(driver.title)
    search_bar = driver.find_element(by=By.ID, value="js-site-search-input")
    search_bar.clear()
    search_bar.send_keys(f"{keyWord}")
    search_bar.submit()

    # Wait for the search results to load
    time.sleep(5)

    # Scroll down the page to load more results
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract DOM all product prices
    # xpath = '//*[@id="js-hits"]/div/div/ol/li/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/span'
    xpath2 = "//div[@id='js-hits']/div/div/ol/li[not(contains(@class, 'some-class'))]//span[contains(@class, 'price')]"

    # time.sleep(30)

    # Extract all product titles
    title_products = driver.find_elements(by=By.XPATH, value='//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
    title_texts = [title.text for title in title_products]

    # Extract all product prices
    price_products = driver.find_elements(By.XPATH, xpath2)
    #price_products= [int(price.text.replace("$", "").replace(".", "")) if price else 0 for price in price_products]
    price_products= [0 for price in title_texts]

    # Extract all product links
    link_elements = driver.find_elements(By.XPATH, '//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
    links_products = [link.get_attribute("href") for link in link_elements]

    #Extract all images links
    image_elements = driver.find_elements(By.XPATH, '//a[@class="js-algolia-product-click"]/img[@srcset]')
    image_urls = [f"https://www.ktronix.com{element.get_attribute('srcset').split(', ')[0].split(' ')[0]}" for element
                  in image_elements]

    marcas = ['Xiaomi', 'Sony', 'Kalley', 'Braun', 'Maytag', 'Realme', 'Alcatel', 'Challenger', 'Alexa', 'Babyliss',
              'Honor', 'TCL', 'LG', 'Nokia', 'Huawei', 'Haceb', 'Panasonic', 'Lenovo', 'Whirlpool', 'MSI', 'Gama',
              'Zte', 'Conair', 'Remington', 'Samsung', 'Oppo', 'Mabe', 'Canon', 'Asus', 'Electrolux', 'iPhone', 'GE',
              'Philips', 'Acer', 'Acros', 'vivo', 'ROG', 'Motorola', 'Wahl', 'Fujifilm', 'GoPro', 'Google Home', 'HP',
              'Tecno', 'Legion', 'Moto']

    marcas_productos = []
    for title in title_texts:
        marca_encontrada = False
        for marca in marcas:
            if marca in title:
                marcas_productos.append(marca)
                marca_encontrada = True
                break
        if not marca_encontrada:
            marcas_productos.append("Otra")

    brand_products = ["Ktronix" for i in range(len(links_products))]

    print(title_texts)
    print(price_products)
    print(links_products)
    print(brand_products)
    print(image_urls)
    print(marcas_productos)

    # diccionario
    data_product["titulo"].extend(title_texts)
    data_product["precio"].extend(price_products)
    data_product["link"].extend(links_products)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(image_urls)
    data_product["empresa"].extend(marcas_productos)

    time.sleep(5)
    driver.close()

    return data_product
