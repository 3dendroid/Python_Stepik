s = str (input ())

pluses = 0
stars = 0

for i in range (len (s)):
    if s[i] == '+':
        pluses += 1
    elif s[i] == '*':
        stars += 1

print (f"Символ + встречается {pluses} раз")
print (f"Символ * встречается {stars} раз")
