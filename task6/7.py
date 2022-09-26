from turtle import *


def move(x, y):
    global a, b
    a += x
    b += y
    goto(a * scale, b * scale)


color('red', 'yellow')

scale = 20

a, b = 0, 0
for i in range(3):
    move(10, 10)
    move(3, -6)
    move(-9, 3)

penup()
for x in range(0 * scale, (10 + 4 * 3) * scale, 1 * scale):
    for y in range(0 * scale, (15 + 13) * scale, 1 * scale):
        goto(x, y)
        stamp()

done()
