def f1(a):
    return int('Z', 36) * 55**3 + a * 55**2 + int('Y', 36) * 55 + int('X', 36)


def f2(a):
    return 2 * 55**3 + int('X', 36) * 55**2 + a * 55 + int('Y', 36)


for a in range(55):
    if (f1(a) - f2(a)) % 29 == 0:
        print(a)

print(f1(23) - f2(23))
print(f1(52) - f2(52))
print(f1(23) - f2(23) - f1(52) + f2(52))
# 86130