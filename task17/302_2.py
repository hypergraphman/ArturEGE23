data = list(map(int, open('17-302.txt').readlines()))

mn = min(filter(lambda x: x % 21 == 0, data))

for i in range(1, len(data)):
    el1, el2 = data[i - 1], data[i]
    if (el1 + el2)
