s1, s2 = input (), input ()
p1, p2 = '', ''

for i in range (len (s1)):
    if s1[i].isalpha ():
        p1 += s1[i]

for i in range (len (s2)):
    if s2[i].isalpha ():
        p2 += s2[i]

if p1.lower () == p2.lower ():
    print ('YES')
else:
    print ('NO')

# a, b = [''.join([i for i in input() if i.isalpha()]) for _ in range(2)]
# print('YES' if a.lower() == b.lower() else 'NO')
