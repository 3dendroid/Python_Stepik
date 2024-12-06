lines = [input () for i in range (4)]

maxx = ord (max (lines)[-1])
minn = ord (min (lines)[-1])

digit = (maxx * minn) ** 2

print (digit)
