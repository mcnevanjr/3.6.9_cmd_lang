import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    time.sleep(30)
    #проверим наличие кнопки добавления в корзину
    button = browser.find_element_by_css_selector(".add-to-basket > button")
    assert button.is_displayed(), "Кнопка добавления товара в корзину отсутствует"
