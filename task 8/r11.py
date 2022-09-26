from itertools import permutations, product

alf = 'skola'
count = 0
for word in product(alf, repeat=3):
    word = ''.join(word)
    if word.count('k') == 1:
        count += 1
print(count)