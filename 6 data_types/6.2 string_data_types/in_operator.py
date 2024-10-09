s = 'https://pygen.ru/'
if 'a' in s:
    print ('Введенная строка содержит символ: а')
else:
    print ('Введенная строка не содержит символ: а')

s = 'Alpha'
print ('p' in s)
print ('P' in s)

language1 = 'JavaScript'
language2 = 'Java'

print (language1 in language2)
print (language2 in language1)

digits = '0123456789'

print ('45' in digits)
print ('09' in digits)

if s in 'abc123abc':
    print ('YES')
else:
    print ('NO')

# s = 'abcabc'
# s = '321'
# s = 'bc2'
# s = 'bca'
# s = '3ab'
# s = 'a'
# s = '123abc'
# s = '23'
# s = '1'
