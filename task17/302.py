from itertools import pairwise


def is_square(n):
    q = int(n ** 0.5)
    return q * q == n


data = list(map(int, open("17-302.txt")))
sorted_data = sorted(data)
counter = 0
min_of_data = 0
for el in sorted_data:
    if el % 21 == 0:
        min_of_data = el
        break

for el1, el2 in pairwise(data):
    average = (el1 + el2) / 2
    if is_square(abs(average - min_of_data)):
        print(el1, el2)
        counter += 1

print(counter)
