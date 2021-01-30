from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #input1 = browser.find_element_by_css_selector(" div > [placeholder='Input your name'] ")
    #input1.send_keys("Этот")
    #input2 = browser.find_element_by_css_selector(" div > [placeholder= 'Input your email'] ")
    #input2.send_keys("Курс")
    #input1 = browser.find_element_by_css_selector(" [ class= 'form-control third' ] ")
    #input1.send_keys("Говно")

    input1 = browser.find_element_by_css_selector(" div > [ class= 'form-control first' ] ")
    input1.send_keys("Этот")
    input2 = browser.find_element_by_css_selector(" div > [ class= 'form-control second' ] ")
    input2.send_keys("Курс")
    input3 = browser.find_element_by_css_selector(" div > [ class= 'form-control third' ] ")
    input3.send_keys("Говно")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()