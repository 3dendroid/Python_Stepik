# # a**2 + b**2 + c**2 + d**2 = e**2
# total = 0

# for a in range(1, 150):
#     for b in range(a, 150):
#         for c in range(b, 150):
#             for d in range(c, 150):
#                 for e in range(d, 150):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         total += 1
#                         print(a + b + c + d + e)


from numba import njit


@njit
def get_solution():
    total = 0
    for a in range(1, 151):
        for b in range(1, 151):
            for c in range(1, 151):
                for d in range(1, 151):
                    for e in range(1, 151):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            total += 1
                            print(a, b, c, d, e)
                            print('a + b + c + d + e =', a + b + c + d + e)
    print('Общее количество натуральных решений =', total)


if __name__ == "__main__":
    get_solution()