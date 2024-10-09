a = int (input ())

first = a // 100
second = (a // 10) % 10
thrid = a % 10

max = max (first, second, thrid)
min = min (first, second, thrid)
middle = (first + second + thrid) - (max + min)

if max - min == middle:
    print ('Число интересное')
else:
    print ('Число неинтересное')
