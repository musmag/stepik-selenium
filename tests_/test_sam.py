import pytest
from selenium import webdriver
import time
import math



@pytest.fixture
def browser():
    print("\nСТАРТУЕМ ПАЦАНЫ")
    browser = webdriver.Chrome()
    yield browser
    print("\nВЫСКАКИВАЕМ НАХУЙ")
    browser.quit()

class TestUFO():

    @pytest.mark.parametrize ('ssil', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_first(self, browser, ssil):
        answer = math.log(int(time.time()))
        link1 = f'https://stepik.org/lesson/{ssil}/step/1'
        browser.get(link1)
        browser.implicitly_wait(5)
        element = browser.find_element_by_tag_name('textarea')
        element.send_keys(str(answer))
        browser.find_element_by_class_name('submit-submission').click()
        correct_te = browser.find_element_by_tag_name('pre')
        correct = correct_te.text
        assert correct == "Correct!"
        time.sleep(1)
