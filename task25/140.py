def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


# for i in range(701, 12000, 2):
#     if len(divs(i)) == 2 and len(divs(i + 10)) == 2 and 854321 <= i * (i + 10) <= 10876540:
#         print(i * (i + 10), i)

for i in range(854321, 10876540 + 1):
    d = divs(i)
    if len(d) == 4 and d[2] - d[1] == 10:
        print(i, d[1])

# 887339 937
# 944759 967
# 1028171 1009
# 1052651 1021