import time
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_css_selector('input[class="form-control first"][required]')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_css_selector('input[class="form-control second"][required]')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector('input[class="form-control third"][required]')
    input3.send_keys("blabla@Smolensk.ru")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()
