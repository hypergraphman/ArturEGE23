def f(n):
    res = ''
    for d in str(n):
        res += f'{int(d):4b}'
    res = res.replace('0', ' ')
    res = res.replace('1', '0')
    res = res.replace(' ', '1')
    return int(res, 2)


i = 1
while f(i) != 151:
    i += 1
print(i)