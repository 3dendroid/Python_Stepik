s = input ()

for i in range (64):
    b = ord ('А') + i
    if str (b) in s:
        s = s.replace (f'[u-{b}]', chr (b))
print (s)
