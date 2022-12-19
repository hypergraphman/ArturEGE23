f = open('26.txt')
s, n = map(int, f.readline().split())
data = []
for _ in range(n):
    data.append(int(f.readline()))
data.sort()
i = 0
while s - data[i] >= 0:
    s -= data[i]
    i += 1
print(i)

s += data[i - 1]
max_v = data[i - 1]
while s - data[i] >= 0:
    max_v = data[i]
    i += 1

print(max_v)