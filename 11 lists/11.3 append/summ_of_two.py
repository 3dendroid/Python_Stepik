n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

sums = [nums[i]+nums[i+1] for i in range(n-1)]
print(sums)