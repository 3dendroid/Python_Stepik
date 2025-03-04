l = [int(i) for i in input().split()]

max_l = max(l)
min_l = min(l)

for i in range(len(l)):
    if l[i] == max_l:
        l[i] = min_l
    elif l[i] == min_l:
        l[i] = max_l

print(*l)



