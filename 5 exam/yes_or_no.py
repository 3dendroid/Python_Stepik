digit = int(input())

if digit % 2 != 0:
    print('YES')
elif (2 <= digit <= 5) and digit % 2 == 0:
    print('NO')
elif (6 <= digit <= 20) and digit % 2 == 0:
    print('YES')
elif (digit > 20) and digit % 2 == 0:
    print('NO')
