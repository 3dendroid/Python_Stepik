# number = int(input())
# if number % 2 == 0:
#     print('Это число чётное. ')
# else:
#     print('Это число нечётное.')


# def is_even(number):
#     if number % 2 == 0:
#         return 'Это число чётное.'
#     else:
#         return 'Это число нечётное.'
# print(is_even(544))

# model = int(input())
# while model != 100 and model != 200 and model != 300:
#     print('Допустимыми номерами моделей являются 100, 200 или 300.')
#     model = int(input())

def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False
print(is_invalid(100))