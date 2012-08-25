from turtle import *

def draw_hexagon(size):
    fill(True)
    for i in range(6):
        forward(size)    
        left(60)
    fill(False)

def draw_meahexa(linesize, size):
    for i in range(6):
        if i % 2:
            color('red')
        else:
            color('blue')
        draw_hexagon(size)
        forward(linesize)
        right(60)

draw_meahexa(30, 80)



