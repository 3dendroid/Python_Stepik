s = input ()
minn = "яя"
maxx = "А"

while s != 'КОНЕЦ':
    if s < minn:
        minn = s
    if s > maxx:
        maxx = s
    s = input ()

print (f'Минимальная строка ⬇️: {minn}')
print (f'Максимальная строка ⬆️: {maxx}')
