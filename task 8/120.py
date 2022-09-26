from itertools import permutations, product

alf = 'prikaz'
words = list(permutations(alf, r=4))
s = set()
for word in words:
    word = ''.join(word)
    if word.count('a') + word.count('i') <= 1:
        s.add(word)

print(len(s))