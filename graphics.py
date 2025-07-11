from turtle import *
import colorsys 
bgcolor("black")
title("studymuch")
pensize(3)
speed(0)
h=160
for i in range(140):
    color = colorsys.hsv_to_rgb(h,1,1)
    pencolor(color)
    h+= 0.01
    circle(i ,100)
    right(80)
    circle(i, -50)
done()    