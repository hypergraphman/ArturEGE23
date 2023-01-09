f = open('26-k6.txt')
n, k = map(int, f.readline().split())
data = []
for i in range(n):
    weigth, cost = map(int, f.readline().split())
    data.append((cost / weigth, weigth, cost))
data.sort(key=lambda x: (x[0], -x[1]))

# print(sum(map(lambda x: x[1], data[:k])))
s = 0
for el in data[:k]:
    s += el[1]
print(s)

# print(max(data[:k], key=lambda x: x[1])[2])
max_el = data[0]
for el in data[:k]:
    if el[1] > max_el[1]:
        max_el = el
print(max_el[2])