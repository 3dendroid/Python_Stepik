letters = 'АБВГДЕЖЗИЙКЛМНОП'
digits = '0123456789'

for i in range (int (input ())):
    s = input ().upper ()
    if len (s) == 2 and s[0] in digits and s[1] in letters:
        print ('YES')
    else:
        print ('NO')
