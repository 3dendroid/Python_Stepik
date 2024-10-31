s = 'aabbAA111ccDDaa'
print (s.isalnum ())
print (s.isalpha ())
print (s.isdigit ())

print ('Cyberpunk 2077'.isalnum ())

print ('Cyberpunk'.isalnum ())
print ('2077'.isalnum ())

s = 'aabb!@#$11cc'
print (s.islower ())

s = 'AAb!@#$11CC'
print (s.isupper ())

print ('2024-05-19'.islower ())
print ('2024-05-19'.isupper ())

s = '    abbc    '
print (s.isspace ())
