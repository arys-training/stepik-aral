import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(3)
    try:
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket3")
    except:
        print("\033[1;31;91mНа странице отсутствует кнопка добавления в корзину\033[0m")
        raise
    finally:
        browser.quit()

# pytest --language=es test_items.py
# pytest --language=fr -s --tb=line test_items.py
