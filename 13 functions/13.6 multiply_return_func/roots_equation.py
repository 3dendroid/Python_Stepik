from math import sqrt


# объявление функции
def solve(a, b, c):
    D = (b * b) - 4 * a * c
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return (x1, x2) if x1 < x2 else (x2, x1)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
