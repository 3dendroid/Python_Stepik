n = int (input ())

for i in range (1, n + 1):
    s = str (input ().strip ())

    if s.isspace () == True or len (s) == 0:
        print (f'{i}: COMMENT SHOULD BE DELETED', sep='')
    else:
        print (f'{i}: {s}', sep='')
