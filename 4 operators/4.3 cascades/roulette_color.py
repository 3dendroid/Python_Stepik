a = int (input ())

if a == 0:
    print ('зеленый')
elif a == 2 or a == 4 or a == 6 or a == 8 or a == 10 or a == 11 or a == 13 or a == 15 or a == 17 or a == 20 or a == 22 or a == 24 or a == 26 or a == 28 or a == 29 or a == 31 or a == 33 or a == 35 % 2 == 0:
    print ('черный')
elif a == 1 or a == 3 or a == 5 or a == 7 or a == 9 or a == 12 or a == 14 or a == 16 or a == 18 or a == 19 or a == 20 or a == 21 or a == 23 or a == 25 or a == 27 or a == 30 or a == 32 or a == 34 or a == 36 % 2 == 0:
    print ('красный')
else:
    print ('ошибка ввода')  # digit 35 not working

## code from chatgpt------------------------------------------------
# a = int(input())

# if a == 0:
#     print('зеленый')
# elif a in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
#     print('черный')
# elif a in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
#     print('красный')
# else:
#     print('ошибка ввода')


## code from chatgpt-----------------------------------------------------------
# a = int(input())

# black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
# red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


# if a == 0:
#     print('зеленый')
# elif a in black_numbers:
#     print('черный')
# elif a in red_numbers:
#     print('красный')
# else:
#     print('ошибка ввода')
