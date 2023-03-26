from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ждем загрузки страницы
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()