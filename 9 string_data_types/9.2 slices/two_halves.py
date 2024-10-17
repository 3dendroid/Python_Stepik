s = str (input ())

split = len (s) // 2 + len (s) % 2

print (s[split:] + s[:split])
