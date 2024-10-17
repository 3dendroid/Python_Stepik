s = 'abcdefghij'

print (s[2:5])
print (s[0:6])
print (s[2:7])
print (s[2:])
print (s[:7])

print (s[1:7:2])
print (s[-3:])
print (s[:-3])

print (s[::-1])  # reverse

print (s[1:7:2])
print (s[3::2])
print (s[:7:3])
print (s[::2])
print (s[::-1])
print (s[::-2])

# s = 'abcdefghij'
# s[2:5] --> cde -->строка состоящая из символов с индексами 2, 3, 4
# s[:5] --> abcde -->первые пять символов строки
# s[5:]	--> fghij -->строка состоящая из символов с индексами от 5 до конца
# s[-2:] --> ij	 -->последние два символа строки
# s[:] --> abcdefghij -->вся строка целиком
# s[1:7:2] --> bdf --> строка состоящая из каждого второго символа с индексами от 1 до 6
# s[::-1] --> jihgfedcba --> строка в обратном порядке, так как шаг отрицательный
