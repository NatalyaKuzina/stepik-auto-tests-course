import time
import math
from selenium import webdriver

try: 
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element_1 = browser.find_element_by_css_selector('span[id="num1"]')
    x_1 = x_element_1.text
    x_element_2 = browser.find_element_by_css_selector('span[id="num2"]')
    x_2 = x_element_2.text    
    y = x_1 + x_2
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='y']").click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(10)
    browser.quit()
