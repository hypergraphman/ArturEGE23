def f(x):
    n1 = int(f'123{x}5', 15)
    n2 = int(f'1{x}233', 15)
    return n1 + n2


i = 0
while f(i) % 14 != 0:
    i += 1
print(f(i) // 14)