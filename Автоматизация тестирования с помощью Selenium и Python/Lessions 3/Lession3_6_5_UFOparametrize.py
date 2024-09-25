import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_many_sites(browser, url):
    try:
        link = f"{url}"
        # browser = webdriver.Chrome
        browser.get(link)
        browser.implicitly_wait(2)
        # time.sleep(10)

        button = browser.find_element(By.XPATH, '//*[@id="ember458"]')
        button.click()
        login = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        login.send_keys("type login here")
        password = browser.find_element(By.XPATH, '//*[@name="password"]')
        password.send_keys("type pass here")
        submit = browser.find_element(By.XPATH, '//*[@type="submit"]')
        submit.click()
        time.sleep(5)

        answer = math.log(int(time.time())+2)
        numbers = browser.find_element(By.XPATH, '//*[@placeholder="Напишите ваш ответ здесь..."]')
        numbers.send_keys(answer)
        otpravka = browser.find_element(By.XPATH, '//*[@class="submit-submission"]')
        otpravka.click()

        time.sleep(5)
        message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')

        f = open("suda.txt", "a")
        f.write(message.text)
        f.close()

        assert "Correct!" in message.text

    finally:
        time.sleep(2)
        browser.quit()
