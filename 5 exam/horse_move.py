x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if abs((x1 - x2) * (y1 - y2)) == 2:
    print('YES')
else:
    print('NO')