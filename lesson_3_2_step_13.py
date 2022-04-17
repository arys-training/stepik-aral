from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):

    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CLASS_NAME, "first_block .form-control.first").send_keys("First Name")
        browser.find_element(By.CLASS_NAME, "first_block .form-control.second").send_keys("Last Name")
        browser.find_element(By.CLASS_NAME, "first_block .form-control.third").send_keys("my@email.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", \
            "Registration #1 is failed")

    def test_registration2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CLASS_NAME, "first_block .form-control.first").send_keys("First Name")
        browser.find_element(By.CLASS_NAME, "first_block .form-control.second").send_keys("Last Name")
        browser.find_element(By.CLASS_NAME, "first_block .form-control.third").send_keys("my@email.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", \
            "Registration #2 is failed")

if __name__ == "__main__":
    unittest.main()
