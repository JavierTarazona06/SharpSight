from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import undetected_chromedriver as uc
import time


def searchProduct(keyWord, data_product:dict, driver:webdriver.Chrome) -> dict:
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get("https://www.linio.com.co/")
    driver.maximize_window()

    def simulate_human_behavior(a, b):
        time.sleep(random.uniform(a, b))  # Agregar un retraso aleatorio

    print(driver.title)
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[name="q"].form-control.search-bar-input')
    search_bar.clear()
    search_bar.send_keys(f"{keyWord}")
    search_bar.submit()

    time.sleep(5)
    #TITLES

    elements = driver.find_elements(By.CLASS_NAME, 'title-section')
    titles_products = [element.text for element in elements]

    #Prices
    elements_prices = driver.find_elements(By.CLASS_NAME, "price-main-md")
    prices = [int(elemento.text.replace('$','').replace('.','')) for elemento in elements_prices]

    #links products
    links_elements = driver.find_elements(By.CLASS_NAME, "detail-container")
    link_element = [link.get_attribute("href") for link in links_elements if
                    link is not None and link.get_attribute("href") is not None]

   #image links
    img_elements = driver.find_elements(By.CLASS_NAME, "image-container")
    figures = [img.find_element(By.TAG_NAME, "figure") for img in img_elements]
    pictures = [img.find_element(By.TAG_NAME, "picture") for img in figures]
    sources = [img.find_element(By.TAG_NAME, "source") for img in pictures]
    links_img = [source.get_attribute("srcset") or source.get_attribute("data-lazy") for source in sources]
    links_img = [link if link.startswith("http://") else "http://" + link.replace("//", "") for link in links_img]

    links_image = []
    for link in links_image:
        cur_image = link.replace("//", "")
        if str(cur_image) == "None" or cur_image == "nan" or cur_image == None:
            links_image.append("https://blog.up.edu.mx/hubfs/Por%20qu%C3%A9%20el%20producto%20es%20lo%20m%C3%A1s%20importante%20para%20una%20estrategia%20comercial%20exitosa.png")
        else:
            links_image.append(cur_image)


    marcas = ['GE', 'HP', 'LG', 'TCL', 'ROG', 'Xiaomi', 'Kalley', 'Braun', 'Maytag', 'Realme', 'Alcatel', 'Challenger', 'Alexa', 'Babyliss',
              'Honor', 'Nokia', 'Huawei', 'Haceb', 'Panasonic', 'Lenovo', 'Whirlpool', 'MSI', 'Gama',
              'Zte', 'Conair', 'Remington', 'Samsung', 'Oppo', 'Mabe', 'Canon', 'Asus', 'Electrolux', 'iPhone', 'Philips', 
              'Acer', 'Acros', 'vivo', 'Motorola', 'Wahl', 'Fujifilm', 'GoPro', 'Google Home', 'Tecno', 'Legion', 'Moto', 'Apple', 
              'Nintendo', 'Microsoft', 'Sony']
    
    #Evitar que no consiga todas las imagenes: Arreglo temporal (Temporal fix)
    if len(links_image) == 0:
         cur_image = "https://blog.up.edu.mx/hubfs/Por%20qu%C3%A9%20el%20producto%20es%20lo%20m%C3%A1s%20importante%20para%20una%20estrategia%20comercial%20exitosa.png"
    else:
        cur_image :str = links_image[0]
    for i in range(len(titles_products)-len(links_image)):
         links_image.append(cur_image)

    marcas_productos = []
    for title in titles_products:
        marca_encontrada = False
        for marca in marcas:
            if marca.lower() in title.lower():
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
    print(links_img)
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


