from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    # return str(int(x)+int(z))


try:
    # Открываем браузер+страницу
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение Х
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    # Находим кнопку
    button = browser.find_element(By.TAG_NAME, "button")

    # через скрипт скроллим страницу до низу
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    input2 = browser.find_element(By.XPATH, '//*[@type="checkbox"]').click()
    input3 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]').click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
