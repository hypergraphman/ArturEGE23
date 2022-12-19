c = 0
for i in range(2015, 3239):
    if sum(map(int, str(i))) > sum(map(int, str(i + 1))):
        c += 1
print(c)