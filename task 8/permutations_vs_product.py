from itertools import permutations, product

alf = 'abc'

print(*product(alf, repeat=3))
for let1 in alf:
    for let2 in alf:
        for let3 in alf:
            print(let1, let2, let3)

print(*permutations(alf))
