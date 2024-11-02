s = str (input ())

digits = '0123456789'
words = 'АВЕКМНОРСТУХ'
space = '_'

if ((len (s) == 10 and s[9] in digits or len (s) == 9) and s[6] == space and s[0] in words and s[4] in words and s[
    5] in words):
    print ('YES')
else:
    print ('NO')
