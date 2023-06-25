from selenium import webdriver
from selenium.webdriver.common.by import By
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

    # Extract all product titles
    title_products = driver.find_elements(by=By.XPATH, value='//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
    title_texts = [title.text for title in title_products]

    # Extract all product prices
    price_products = driver.find_elements(By.CLASS_NAME, "price")
    price_values = [int(price.text.strip().replace('$', '').replace('.','')) for price in price_products if price.text.strip()]

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
              'Tecno', 'Legion', 'Moto', 'Apple', 'Nintendo', 'Microsoft', 'Sony']

    marcas_productos = []
    for title in title_texts:
        marca_encontrada = False
        for marca in marcas:
            if marca.lower() in title.lower():
                marcas_productos.append(marca)
                marca_encontrada = True
                break
        if not marca_encontrada:
            marcas_productos.append("Otra")

    brand_products = ["Ktronix" for i in range(len(links_products))]

    print(title_texts)
    print(price_values)
    print(links_products)
    print(brand_products)
    print(image_urls)
    print(marcas_productos)

    # diccionario
    data_product["titulo"].extend(title_texts)
    data_product["precio"].extend(price_values)
    data_product["link"].extend(links_products)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(image_urls)
    data_product["empresa"].extend(marcas_productos)

    time.sleep(5)
    driver.close()

    return data_product
