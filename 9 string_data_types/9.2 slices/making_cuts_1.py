s = str (input ())

count = len (s)
repeat = s * 3
first_symbol = s[:1]
first_three_symbols = s[:3]
last_three_symbols = s[-3:]
reverse = s[::-1]
first_last_delete = s[1:-1:]

print (count)
print (repeat)
print (first_symbol)
print (first_three_symbols)
print (last_three_symbols)
print (reverse)
print (first_last_delete)

# s = input ()
# print (len (s))
# print (s * 3)
# print (s[0])
# print (s[0:3])
# print (s[-3:])
# print (s[::-1])
# print (s[1:-1])

# s = input ()
# print (len (s), s[:] * 3, s[0], s[:3], s[-3:], s[::-1], s[1:-1], sep='\n')
