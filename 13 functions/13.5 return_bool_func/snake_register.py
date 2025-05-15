# объявление функции
def convert_to_python_case(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, '_' + i.lower())
    return text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
