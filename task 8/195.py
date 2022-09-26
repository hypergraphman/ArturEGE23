from itertools import permutations, product

s = set()
for v1 in 'sepia':
    for i in range(2, 7):
        for word in product('eia', repeat=i):
            word = v1 + ''.join(word)
            if word.count('e') <= 2 and word.count('i') <= 2 and word.count('a') <= 2:
                s.add(word)
print(len(s))
