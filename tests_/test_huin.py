from selenium import webdriver
import time
import math

link = 'https://stepik.org/lesson/236896/step/1'
browser = webdriver.Chrome()
browser.get(link)
answer = math.log(int(time.time()))

browser.implicitly_wait(5)



option1 = browser.find_element_by_tag_name('textarea')
option1.send_keys(str(answer))