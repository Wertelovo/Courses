from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ждем, пока цена не станет равной 100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем на кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    answer = math.log(abs(12*math.sin(x)))

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(answer))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получаем число из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split()[-1])
    alert.accept()

finally:
    # Закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()