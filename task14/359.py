def f1(x, y):
    return 7 * 25**5 + y * 25**4 + 2 * 25**3 + 3 * 25**2 + x * 25 + 5


def f2(x, y):
    return 6 * 11**4 + 7 * 11**3 + x * 11**2 + 9 * 11 + y


for x in range(11):
    for y in range(11):
        if (f1(x, y) + f2(x, y)) % 131 == 0:
            print(x, y)


print((f1(5, 10) + f2(5, 10)) / 131)
