n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
        for k in range(j + 1):
            print('*', end='')
    print()

# continue to next
