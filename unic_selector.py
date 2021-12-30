import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = driver.find_elements_by_tag_name ("input")
    for element in elements:
        element.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)

    # После выполнения всех действий мы не должны забыть закрыть окно браузера
    driver.quit()
