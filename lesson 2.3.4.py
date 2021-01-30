from selenium import webdriver
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("[class='btn btn-primary']").click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button1 = browser.find_element_by_css_selector("[class='btn btn-primary']").click()
