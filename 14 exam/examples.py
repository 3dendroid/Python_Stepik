# объявление функции
def draw_triangle():
    for i in range(1, 9):
        print(' ' * (8 - i) + '*' * (2 * i - 1))


# основная программа
draw_triangle()  # вызов функции
