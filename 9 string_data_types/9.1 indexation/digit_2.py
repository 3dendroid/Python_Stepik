n = str (input ())
flag = 'Цифр нет'

for i in range (len (n)):
    if n[i].isdigit ():
        flag = 'Цифра'

print (flag)
