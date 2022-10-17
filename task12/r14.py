for x in range(50):
    for y in range(50):
        for z in range(50):
            f1 = 2 * x + 3 * y + 6 * z
            f2 = y + z
            if f1 == 186 and f2 == 26:
                print(x, y, z, x + y + z + 2)
    