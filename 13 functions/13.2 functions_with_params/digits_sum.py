# объявление функции
def print_digit_sum(num):
    # print(sum(map(int, str(num))))
    print(sum(int(i) for i in list(str(num))))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
