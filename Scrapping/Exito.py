from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Crear una instancia del WebDriver
PATH = "/Users/knsmolina.28/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(PATH)

# Navegar hacia la página web y buscar el nombre
driver.get("https://www.exito.com/")
print(driver.title)

# Esperar a que el elemento esté presente
time.sleep(5)
search_bar = driver.find_element(By.TAG_NAME, "input")
# Realizar acciones en el elemento
search_bar.clear()
search_bar.send_keys("iphone 14")
search_bar.send_keys(Keys.RETURN)

time.sleep(5)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        time.sleep(10)
        break
    last_height = new_height

# Esperar un poco más para asegurarse de que los elementos se carguen completamente

#time.sleep(20)

titles_products = driver.find_elements(By.XPATH, '//*[@id="gallery-layout-container"]/*/section/a/article/div[2]/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/div/h3/span')
titles_products = [title.text for title in titles_products]
print(titles_products)

price_texts = driver.find_elements(By.XPATH, '//*[@id="gallery-layout-container"]/*/section/a/article/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div[2]/div/span')
price_texts = [price.text for price in price_texts]
print(price_texts)


links_elements = driver.find_elements(By.XPATH, '//*[@id="gallery-layout-container"]//section/a')
links = [link.get_attribute("href") for link in links_elements]
print(links)

data_products = {
    "name_product": titles_products,
    "price-product": price_texts,
    "link_product": links
}
df = pd.DataFrame(data_products)
df.to_csv("exito.csv", index = True, sep = ";")

# Cerrar el navegador
driver.quit()
