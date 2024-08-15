from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    # return str(int(x)+int(z))


try:
    # Открываем браузер+страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//*[@name="firstname"]')
    input1.send_keys("Imya")
    input2 = browser.find_element(By.XPATH, '//*[@name="lastname"]')
    input2.send_keys("Familiya")
    input3 = browser.find_element(By.XPATH, '//*[@name="email"]')
    input3.send_keys("Pochta")
    input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
    input4.send_keys(file_path)

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
