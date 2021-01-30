from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

first_num = browser.find_element_by_id('num1')
chislo1 = first_num.text

second_num = browser.find_element_by_id('num2')
chislo2 = second_num.text

summa_chis = int(chislo1) + int(chislo2)
s = str(summa_chis)
print(s)
#browser.find_element_by_id("dropdown").click()

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(s)
#эта хуйня работает с селектором. сначала выбирает сам селектор, потом значение из него которое мы задаем

pizda = browser.find_element_by_class_name('btn.btn-default').click()