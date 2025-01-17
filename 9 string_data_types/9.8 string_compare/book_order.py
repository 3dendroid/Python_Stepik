list1 = []
list2 = []
n = int(input())

for i in range(n):
    c = input().strip()

    list1.append(c[:c.find('')] + c[c.find('«'):])
    list2.append(c[:c.find('')] + c[c.find('«'):])

list2.sort()

if list1 == list2:
    print('NO')
else:
    print('YES')
