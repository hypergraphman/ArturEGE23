from re import fullmatch

for n in range(141, 10**8, 141):
    if fullmatch(r'1234\d*7', str(n)):
        print(n, n // 141)