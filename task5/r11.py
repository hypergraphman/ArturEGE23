def f(n):
    step1 = f'{n:b}'
    step2 = step1[1:]
    step3 = int(step2, 2)
    return n - step3


def f1(n):
    return 2 ** (len(f'{n:b}') - 1)


ans = set()
for i in range(500, 5000 + 1):
    ans.add(f1(i))

print(ans)
print(len(ans))