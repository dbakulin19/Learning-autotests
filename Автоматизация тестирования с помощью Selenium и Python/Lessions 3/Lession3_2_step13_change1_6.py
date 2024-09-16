from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):  # Cоздаем класс, который наследуется от TestCase

    def test_registration_should_pass(self):  # Делаем из функций методы, ссылаясь на self

    # Входные данные
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your first name')]")
    input1.send_keys("FIRST name")
    input2 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your last name')]")
    input2.send_keys("last NAME")
    input3 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your email')]")
    input3.send_keys("EmAiL@test.test")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    browser.quit()

    def test_registration_should_fail(self):

    # Входные данные
    link2 = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link2)

    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your first name')]")
    input1.send_keys("FIRST name")
    input2 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your last name')]")
    input2.send_keys("last NAME")
    input3 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your email')]")
    input3.send_keys("EmAiL@test.test")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # Закрываем браузер после всех манипуляций
    browser.quit()

if __name__ == "__main__":
    unittest.main()  # Заменяем запуск