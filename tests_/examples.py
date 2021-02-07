#форматирование - подставление пользовательских значений в строку
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

#сооставные сообщения об ошибках
assert self.is_element_present('create_class_button', timeout=30), "No create class button"

#Форматирование строк с помощью f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

#для считывания текста на странице
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"


#задача из урока 3.2.8

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f" expected {expected_result}, got {actual_result}"

#задача из урока 3.2.9
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"