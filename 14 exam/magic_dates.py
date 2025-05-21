# объявление функции
def is_magic(date):
    d, m, g = date.split('.')
    d, m = int(d), int(m)
    last_two = int(g[2:])

    if d * m == last_two:
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
