print(*[(int(x) ** 2) for x in input().split() if (int(x) ** 2) % 2 == 0 and (int(x) ** 2) % 10 != 4])
