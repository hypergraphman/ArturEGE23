from time import time

k = 1000000000000
st = time()
for i in range(10_000_000):
    k /= 2
    k += 1
print(time() - st)
