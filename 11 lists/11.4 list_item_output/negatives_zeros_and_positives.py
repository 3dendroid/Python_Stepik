temp = []
negatives = []
zeros = []
positives = []

n = int(input())
for i in range(n):
    temp.append(int(input()))
    if temp[i] < 0:
        negatives.append(temp[i])
    if temp[i] == 0:
        zeros.append(temp[i])
    if temp[i] > 0:
        positives.append(temp[i])

print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
