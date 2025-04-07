# def draw_box(height, width):  # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
# draw_box(3, 3)
# print()
# draw_box(5, 5)
# print()
# draw_box(4, 10)

# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)
# n = 5
# m = 7
# draw_box(n, m)
# print(n, m)

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)
# print_number(2,3,11)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)

def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1
print_text('Python', 4)