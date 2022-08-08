def f(n):
    step1 = f'{n:b}'
    try:
        i_last_zero = step1.rindex('0')
    except:
        return 0
    step2 = step1[:i_last_zero] + step1[:2] + step1[i_last_zero + 1:]
    step3 = step2[::-1]
    return int(step3, 2)


i = 1
while f(i) != 123:
    i += 1
print(i)