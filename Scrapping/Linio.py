from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def searchProduct(keyWord, data_product:dict, driver:webdriver.Chrome) -> dict:
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get("https://www.linio.com.co/")

    def simulate_human_behavior(a, b):
        time.sleep(random.uniform(a, b))  # Agregar un retraso aleatorio

    print(driver.title)
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[name="q"].form-control.search-bar-input')
    search_bar.clear()
    search= [f"{keyWord}"]

    search_bar = driver.find_element(by=By.CLASS_NAME, value="nav-search-input")
    search_bar.clear()
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)

    #TITLES
    elements = driver.find_elements(By.CLASS_NAME, 'title-section')
    titles_products = [element.text for element in elements]

    #Prices
    elements_prices = driver.find_elements(By.CLASS_NAME, "price-main-md")
    prices = [elemento.text for elemento in elements_prices]

    #links products
    links_elements = driver.find_elements(By.CLASS_NAME, "detail-container")
    link_element = [link.get_attribute("href") for link in links_elements if
                    link is not None and link.get_attribute("href") is not None]

   #image links
    img_elements = driver.find_elements(By.CLASS_NAME, "image-container")
    figures = [img.find_element(By.TAG_NAME, "figure") for img in img_elements]
    pictures = [img.find_element(By.TAG_NAME, "picture") for img in figures]
    sources = [img.find_element(By.TAG_NAME, "source") for img in pictures]
    links_image = [source.get_attribute("srcset") or source.get_attribute("data-lazy") for source in sources]
    links_image = [link.replace("//", "") for link in links_image]

    marcas = ['Xiaomi', 'Sony', 'Kalley', 'Braun', 'Maytag', 'Realme', 'Alcatel', 'Challenger', 'Alexa', 'Babyliss',
              'Honor', 'TCL', 'LG', 'Nokia', 'Huawei', 'Haceb', 'Panasonic', 'Lenovo', 'Whirlpool', 'MSI', 'Gama',
              'Zte', 'Conair', 'Remington', 'Samsung', 'Oppo', 'Mabe', 'Canon', 'Asus', 'Electrolux', 'iPhone', 'GE',
              'Philips', 'Acer', 'Acros', 'vivo', 'ROG', 'Motorola', 'Wahl', 'Fujifilm', 'GoPro', 'Google Home', 'HP',
              'Tecno', 'Legion', 'Moto']

    marcas_productos = []
    for title in titles_products:
        marca_encontrada = False
        for marca in marcas:
            if marca in title:
                marcas_productos.append(marca)
                marca_encontrada = True
                break
        if not marca_encontrada:
            marcas_productos.append("Otra")

    brand_products = ["Linio" for _ in range(len(titles_products))]

    print(titles_products)
    print(prices)
    print(link_element)
    print(brand_products)
    print(links_image)
    print(marcas_productos)

    data_product["titulo"].extend(titles_products)
    data_product["precio"].extend(prices)
    data_product["link"].extend(link_element)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(links_image)
    data_product["empresa"].extend(marcas_productos)

    time.sleep(5)
    driver.close()

    return data_product


