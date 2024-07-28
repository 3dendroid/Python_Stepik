m = int(input())
n = int(input())

if (m and n / 17) or (m and n % 10 == 9) or (m and n / 3 and 5):
    for i in range(m, n+1):
        print(i)
