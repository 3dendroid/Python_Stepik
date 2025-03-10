n = [int(i) for i in input().split()]

n.sort()
print(*n)
n.sort(reverse=True)
print(*n)