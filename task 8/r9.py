from itertools import permutations, product

alf = 'vualy'
s = set()
for word in permutations(alf):
    word = ''.join(word)
    if not ('yu' in word or 'ya' in word) and word[0] != 'y':
        s.add(word)
print(len(s))