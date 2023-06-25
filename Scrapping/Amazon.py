from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def searchProduct(keyWord, data_product : dict, driver: webdriver.Chrome) -> dict:

    driver.get("https://www.amazon.com/-/es/")

    def simulate_human_behavior():
        time.sleep(random.uniform(2, 10))  # Agregar un retraso aleatorio

    def change_currency():
        elemento = driver.find_element(By.ID, "icp-touch-link-cop")
        elemento.click()

        currency_dropdown_element = driver.find_element(By.ID, "icp-currency-dropdown-selected-item-prompt")
        currency_dropdown_element.click()

        currency_option_element = driver.find_element(By.XPATH, "//a[@data-value='{\"stringVal\":\"COP\"}']")
        currency_option_element.click()

        time.sleep(2)

        back_button = driver.find_element(By.CSS_SELECTOR,
                                          "input.a-button-input[aria-labelledby='icp-save-button-announce']")
        back_button.click()

        time.sleep(2)

    # Cambiar la moneda
    change_currency()

    print(driver.title)
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.clear()
    search_bar.send_keys(f"{keyWord}")
    simulate_human_behavior()
    search_bar.submit()

    # Extract all product titles
    titles = driver.find_elements(By.XPATH, "//h2/a/span")
    titles_products = [element.text for element in titles]
    simulate_human_behavior()

    # Extract all product prices
    elements_prices = driver.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
    prices = [int(price.text.replace(',','')) for price in elements_prices]

    # Extract all product links
    links_elements = driver.find_elements(By.XPATH,
                                          "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    links = [link.get_attribute("href") for link in links_elements]

    # Extract all images links
    image_elements = WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="a-section aok-relative s-image-fixed-height"]//img'))
    )
    image_urls = [image.get_attribute("src") for image in image_elements]

    marcas = ['Xiaomi', 'Sony', 'Kalley', 'Braun', 'Maytag', 'Realme', 'Alcatel', 'Challenger', 'Alexa', 'Babyliss',
              'Honor', 'TCL', 'LG', 'Nokia', 'Huawei', 'Haceb', 'Panasonic', 'Lenovo', 'Whirlpool', 'MSI', 'Gama',
              'Zte', 'Conair', 'Remington', 'Samsung', 'Oppo', 'Mabe', 'Canon', 'Asus', 'Electrolux', 'iPhone', 'GE',
              'Philips', 'Acer', 'Acros', 'vivo', 'ROG', 'Motorola', 'Wahl', 'Fujifilm', 'GoPro', 'Google Home', 'HP',
              'Tecno', 'Legion', 'Moto', 'Apple', 'Nintendo', 'Microsoft', 'Sony']

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

    brand_products = ["Amazon" for i in range(len(links_elements))]
    print(brand_products)

    print(titles_products)
    print(prices)
    print(links)
    print(brand_products)
    print(image_urls)
    print(marcas_productos)

    data_product["titulo"].extend(titles_products)
    data_product["precio"].extend(prices)
    data_product["link"].extend(links)
    data_product["marca"].extend(brand_products)
    data_product["imagen"].extend(image_urls)
    data_product["empresa"].extend(marcas_productos)

    time.sleep(4)
    driver.close()

    return data_product








