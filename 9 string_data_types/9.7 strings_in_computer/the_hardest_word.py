max = -1
total = 0
text = ' '
for i in range (4):
    cnt = 0
    s = input ()
    for j in range (len (s)):
        cnt += ord (s[j])
    if cnt > max:
        max = cnt
        text = s
print (text)
