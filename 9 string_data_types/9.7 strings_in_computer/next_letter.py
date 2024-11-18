s = input ()

if ord (s) == 1071:
    print ('Дальше букв нет')
elif ord (s) < 1071:
    print (chr (ord (s) + 1))
