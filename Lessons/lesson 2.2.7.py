from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_css_selector("[name='firstname']")
option1.send_keys("Koban")

option2 = browser.find_element_by_css_selector("[name='lastname']")
option2.send_keys("Kob Kob")

option3 = browser.find_element_by_css_selector("[name='email']")
option3.send_keys("Kotokob")

current_dir = os.path.abspath(os.path.dirname(__file__))

file_name = "text.txt"
file_path = os.path.join(current_dir, file_name)

element = browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_css_selector("[class='btn btn-primary']").click()


