from re import fullmatch

for n in range(3127, 10**9, 3127):
    if fullmatch(r'12\d*93\d7\d', str(n)):
        print(n)
