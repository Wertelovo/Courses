from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
    x = int(x_element.text)

    # Считаем математическую функцию от x
    y = math.log(abs(12*math.sin(x)))

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR,"#answer")
    answer_input.send_keys(str(y))

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robot_radio = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    robot_radio.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    submit_button.click()

finally:
    # Добавляем задержку, чтобы визуально убедиться, что всё прошло успешно
    time.sleep(5)
    # Закрываем браузер
    browser.quit()
