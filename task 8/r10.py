from itertools import permutations, product

alf = 'kapkan'
s = set()
for word in permutations(alf):
    word = ''.join(word)
    if not ('kk' in word or 'aa' in word):
        s.add(word)
print(len(s))