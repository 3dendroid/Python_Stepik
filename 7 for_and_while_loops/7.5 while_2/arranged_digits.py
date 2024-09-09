num = int(input())

progression = True

while (num % 100 // 10) != 0:
    last_digit = num % 10
    pred_digit = (num // 10) % 10
    if last_digit > pred_digit:
        progression = False
        break
    num = num // 10
if progression == True:
    print('YES')
else:
    print('NO')
