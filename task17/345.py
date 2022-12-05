from itertools import pairwise

a = list(map(int, open('17-345.txt').readlines()))
b = list(filter(lambda x: x % 100 == 52, a))
r = max(b) - min(b)
c = [el1 + el2 for el1, el2 in pairwise(a) if el1 < r <= el2 or el2 < r <= el1]
print(len(c), max(c))
