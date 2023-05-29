from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd


def searchProduct(keyWord, data_product : dict, driver : webdriver.Chrome) -> dict:

    # Navegar hacia la página web y buscar el nombre
    driver.get("https://www.exito.com/")
    print(driver.title)

    # Esperar a que el elemento esté presente
    time.sleep(5)
    search_bar = driver.find_element(By.TAG_NAME, "input")
    # Realizar acciones en el elemento
    search_bar.clear()
    search_bar.send_keys(f"{keyWord}")
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
    price_texts = [int(price.text.replace("$", "").replace(".", "").replace(" ","")) for price in price_texts]
    print(price_texts)


    links_elements = driver.find_elements(By.XPATH, '//*[@id="gallery-layout-container"]//section/a')
    links = [link.get_attribute("href") for link in links_elements]
    print(links)

    brand_products = ["Exito" for i in range(len(links))]
    print(brand_products)

    image_elements = driver.find_elements(By.XPATH,'//img[@class="vtex-product-summary-2-x-imageNormal vtex-product-summary-2-x-image vtex-product-summary-2-x-mainImageHovered"]')
    image_urls = [image.get_attribute("src") for image in image_elements]

    #Evitar que no consiga todas las imagnes: Arreglo temporal (Temporal fix)
    cur_image :str = image_urls[0]
    for i in range(len(titles_products)-len(image_urls)):
         image_urls.append(cur_image)


    print(image_urls)

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
    print(marcas_productos)


    # diccionario
    data_product["titulo"].extend(titles_products)
    data_product["precio"].extend(price_texts)
    data_product["link"].extend(links)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(image_urls)
    data_product["empresa"].extend(marcas_productos)
    
    time.sleep(5)
    driver.close()
    # Cerrar el navegador
    #driver.quit()

    return data_product