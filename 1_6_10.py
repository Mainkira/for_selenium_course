from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements(By.TAG_NAME, 'label')
    inputs = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    # inputs = browser.find_elements(By.XPATH, '//label[contains(text(),"*")]/following::input[1]')
    for i, label in enumerate(labels):
        if label.text[-1] == '*':
            inputs[i].send_keys("текст")


    # elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    # for element in elements:
    #     element.send_keys("Test text")


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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()