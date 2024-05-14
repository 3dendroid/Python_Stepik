a = int(input())

if 1 < a < 10 % 2 or 19 < a < 28 % 2 == 0:
    print('черный')
elif 11 < a < 18 % 2 or 29 < a < 37 % 2 == 0:
    print('красный')
else:
    print('ошибка ввода')

# continue 