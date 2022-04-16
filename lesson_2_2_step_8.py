import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"
"""

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    nameFirst = browser.find_element(By.XPATH, "//input[@name='firstname' and @placeholder='Enter first name']")
    nameFirst.send_keys("Аты-жөні")

    nameLast = browser.find_element(By.XPATH, "//input[@name='lastname' and @placeholder='Enter last name']")
    nameLast.send_keys("Тегі")

    eMail = browser.find_element(By.XPATH, "//input[@name='email' and @placeholder='Enter email']")
    eMail.send_keys("my@mail")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_name = "file_example.txt"

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, file_name)

    # Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file"
    send_file = browser.find_element(By.CSS_SELECTOR, "[type='file']#file")
    send_file.send_keys(file_path)

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
