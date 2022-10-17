def n_to_p(n, p):
    digs = '0123456789ABCDEF'
    r = ''
    while n != 0:
        r = digs[n % p] + r
        n //= p
    return r


num = 49**7 + 7**21 - 7
res = n_to_p(num, 7)
print(res, res.count('6'))