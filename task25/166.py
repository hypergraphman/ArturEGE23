a = []
for m in range(1, 28 + 1, 2):
    for n in range(0, 10 + 1, 2):
        num = 2**m * 7**n
        if 100_000_000 <= num <= 300_000_000:
            a.append((num, m + n))
print(*sorted(a))