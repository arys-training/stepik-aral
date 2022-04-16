from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary' and \
        text()='I want to go on a magical journey!']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    first_window = browser.window_handles[0]

    time.sleep(1)

    input_value = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    y = calc(int(input_value.text))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
