from selenium import webdriver
import math


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox").click()

option2 = browser.find_element_by_css_selector("#robotsRule").click()

option3 = browser.find_element_by_class_name('btn.btn-default').click()





