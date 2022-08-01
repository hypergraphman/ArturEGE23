from itertools import permutations


def f(n):
    mx = 0
    mn = 100
    for el in permutations(str(n), 2):
        num = int(el[0] + el[1])
        if 10 <= num <= 99:
            mx = max(num, mx)
            mn = min(num, mn)
    return mx - mn


i = 100
while f(i) != 40:
    i += 1
print(i)