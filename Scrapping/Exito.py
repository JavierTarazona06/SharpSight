from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm

PATH = "/Users/knsmolina.28/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.exito.com/")

print(driver.title)
search_bar = driver.find_element(by=By.ID, value="downshift-1-input")
search_bar.clear()
search_bar.send_keys("reloj samsung a4")
search_bar.submit()
time.sleep(5)
driver.close()
