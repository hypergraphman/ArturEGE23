def fx(x):
    return x * 22**4 + 2 * 22**3 + 3 * 22**2 + x * 22 + 5


def fy(y):
    return 6 * 13**4 + 7 * 13**3 + y * 13**2 + 9 * 13 + y


for x in range(22):
    for y in range(13):
        if (fx(x) - fy(y)) % 57 == 0:
            print(x, y)


print((fx(0) - fy(6)) / 57)