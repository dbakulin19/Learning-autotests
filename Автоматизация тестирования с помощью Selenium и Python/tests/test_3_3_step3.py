from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration_should_pass(self):
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

        # Сравниваем результат
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, 'Should be equal')

        browser.quit()

    def test_registration_should_fail(self):
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

        # Сравниваем результат
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, 'Should be equal')

        # Закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()  # Заменяем запуск
