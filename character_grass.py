from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 0
xAngle, yAngle = 0,0
angle = 0
while (1):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
    while (y < 600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y + 5
            delay(0.01)
    y = 600
    while (x >0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 5
            delay(0.01)
    x = 0
    while (y >0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y - 5
            delay(0.01)
    y = 0
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x+ math.cos(angle),y + math.sin(angle))
        delay(0.01)
        angle = angle+2

    angle = 0
close_canvas()
    
