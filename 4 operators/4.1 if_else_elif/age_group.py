i = int(input())

try:
    if i <= 13:
        print('детство')
    elif 14 <= i <= 24:
        print('молодость')
    elif 25 <= i <= 59:
        print('зрелость')
    else:
        print('старость')
except ValueError as e:
    print(e)
