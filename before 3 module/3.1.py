from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку сундука и получаем значение атрибута valuex
    treasure_img = browser.find_element(By.ID, "treasure")
    x = int(treasure_img.get_attribute("valuex"))

    # Вычисляем значение функции от x
    y = math.log(abs(12*math.sin(x)))

    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(str(y))

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Добавляем задержку, чтобы визуально убедиться, что всё прошло успешно
    time.sleep(5)
    # Закрываем браузер
    browser.quit()
