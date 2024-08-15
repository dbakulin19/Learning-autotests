from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//img')
    time.sleep(2)
    value = x_element.get_attribute("valuex")
    print("", value)
    x = value
    y = calc(x)

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
