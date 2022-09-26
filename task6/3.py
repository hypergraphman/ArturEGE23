from turtle import *

color('red', 'yellow')

left(90)

scale = 30
for i in range(15):
    forward(4 * scale)
    right(60)

penup()
for x in range(1 * scale, 10 * scale, 1 * scale):
    for y in range(1 * scale, 10 * scale, 1 * scale):
        goto(x, y)
        stamp()

done()
