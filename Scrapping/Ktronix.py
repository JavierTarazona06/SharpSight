from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm

def searchProduct(keyWord):

    PATH = "chromedriver"
    driver = webdriver.Chrome(PATH)
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
    print(title_texts)

    price_products = driver.find_elements(by=By.XPATH, value='//*[@id="js-hits"]/div/div/ol/li/div[2]/div[3]/div[2]/div[1]/div[2]/div/p[2]/span[1]')
    price_products = [price.text for price in price_products]
    print(price_products)

    link_elements = driver.find_elements(By.XPATH, '//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
    links = [link.get_attribute("href") for link in link_elements]
    print(links)

    data_product = {"titulo":title_texts,"precio":price_products,"link":links}

    df = pd.DataFrame(data_product)
    df.to_csv("productos.csv")

    time.sleep(5)
    driver.close()
