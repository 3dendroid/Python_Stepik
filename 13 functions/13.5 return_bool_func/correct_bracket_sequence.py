# объявление функции
def is_correct_bracket(text):
    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
