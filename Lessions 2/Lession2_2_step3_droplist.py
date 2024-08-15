from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

def calc(x):
 return str(int(x)+int(z))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id="num1"]')
    z_element = browser.find_element(By.XPATH, '//*[@id="num2"]')
    x = x_element.text
    z = z_element.text
    y = calc(x)
    print(y)

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))  # ищем элемент со значением "математическое сложение"

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
