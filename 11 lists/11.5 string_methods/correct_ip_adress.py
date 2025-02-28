s = input().split('.')
c = 0

for i in s:
    if 0 <= int(i) <= 255:
        c += 1
    else:
        c = -1

if c == 4:
    print("ДА")
else:
    print("НЕТ")


