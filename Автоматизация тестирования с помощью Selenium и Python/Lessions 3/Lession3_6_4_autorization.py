import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStepik():
    def test_autorization_successful(self):
        try:
            link = "https://stepik.org/lesson/236895/step/1?auth=login"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)
            # time.sleep(10)

            Login = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
            Login.send_keys("dmitrybakulin19@gmail.com")
            Password = browser.find_element(By.XPATH, '//*[@name="password"]')
            Password.send_keys("qwe12131ewq")
            Submit = browser.find_element(By.XPATH, '//*[@type="submit"]')
            Submit.click()

        finally:
            time.sleep(2)
            browser.quit()
