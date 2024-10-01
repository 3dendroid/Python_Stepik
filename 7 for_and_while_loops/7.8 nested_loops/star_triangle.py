n = int (input ())

for i in range (n // 2 + 2):
    print ('*' * i)
for j in range (n // 2, 0, -1):
    print ('*' * j)

#
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
#
# for k in range(n // 2 + 1, -1, -1):
#     for m in range(k + 1):
#         print('*', end='')
#     print()
