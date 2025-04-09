# объявление функции
def draw_triangle(fill, base):
    half = base // 2 + 1

    for i in range(1, half + 1):
        print(fill * i)

    for i in range(half - 1, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())
# вызываем функцию
draw_triangle(fill, base)
