def n_to_p(n, p):
    digs = '0123456789ABCDEF'
    r = ''
    while n != 0:
        r = digs[n % p] + r
        n //= p
    return r


print(n_to_p(194, 5))
print(n_to_p(255, 16))
print(n_to_p(100, 2))
