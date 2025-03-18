# print(*[x for x in input() if '0' <= x <= '9'], sep='')
print(*[x for x in input() if x in x.isdigit() == True], sep='')
