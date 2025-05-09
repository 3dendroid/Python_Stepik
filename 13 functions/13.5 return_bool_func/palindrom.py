# объявление функции
def is_palindrome(text):
    # Оставляем только буквы и цифры, приводим к нижнему регистру
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
