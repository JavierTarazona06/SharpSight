from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from tqdm import tqdm

PATH = "/Users/knsmolina.28/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.ktronix.com/")

print(driver.title)
search_bar = driver.find_element(by=By.ID, value="js-site-search-input")
search_bar.clear()
search_bar.send_keys("iphone 14")
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
#xpath = '//*[@id="js-hits"]/div/div/ol/li/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/span'
xpath2 = "//div[@id='js-hits']/div/div/ol/li[not(contains(@class, 'some-class'))]//span[contains(@class, 'price')]"

#time.sleep(30)

# Extract all product titles
title_products = driver.find_elements(by=By.XPATH, value='//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
title_texts = [title.text for title in title_products]

# Extract all product prices
price_products = driver.find_elements(By.XPATH, xpath2)
price_texts = [price.text for price in price_products]

# Extract all product links
link_elements = driver.find_elements(By.XPATH, '//*[@id="js-hits"]/div/div/ol/li/div[1]/h3/a')
links = [link.get_attribute("href") for link in link_elements]

data_products = {
    "name_product": title_texts,
    "price-product": price_texts,
    "link_product": links
}
df = pd.DataFrame(data_products)
df.to_csv("ktronix.csv", index = True, sep = ";")
driver.quit()







