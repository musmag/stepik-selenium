from selenium import webdriver
import math


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

poisk_sunduka = browser.find_element_by_id('treasure')
sunduk = poisk_sunduka.get_attribute('valuex')
x = sunduk
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox").click()

option2 = browser.find_element_by_css_selector("#robotsRule").click()

option3 = browser.find_element_by_class_name('btn.btn-default').click()

'''Идеальное решение
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/get_attribute.html
browser.get('http://suninjuly.github.io/get_attribute.html')

# Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()'''