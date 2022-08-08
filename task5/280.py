def f(n):
    s1 = sum(filter(lambda x: x % 2, map(int, str(n))))
    s2 = sum(map(int, str(n)[::-2]))
    return abs(s1 - s2)


def f1(n):
    s1 = 0
    for d in str(n):
        d = int(d)
        if d % 2:
            s1 += d
    s2 = 0
    for d in str(n)[::-2]:
        s2 += int(d)
    return abs(s1 - s2)


i = 1
while f1(i) != 29:
    i += 1
print(i)