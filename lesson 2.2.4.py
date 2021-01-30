from selenium import webdriver
import math


link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
print(y)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

option1 = browser.find_element_by_css_selector("#robotCheckbox").click()

option2 = browser.find_element_by_css_selector("#robotsRule").click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#pizda = browser.find_element_by_class_name('btn.btn-default').click()