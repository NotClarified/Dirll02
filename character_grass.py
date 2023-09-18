from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 0
angle = 0
while (1):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)
    while (y < 600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y + 2
            delay(0.01)
    y = 600
    while (x >0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 2
            delay(0.01)
    x = 0
    while (y >0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y - 2
            delay(0.01)
    y = 0
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)
    while(angle < 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x*30, y*30)
            x = x - math.sin(2)
            y = y - math.cos(2)
            delay(0.01)
            angle = angle + 2
    while(angle < 180):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x*30, y*30)
            x = x - math.sin(2)
            y = y + math.cos(2)
            delay(0.01)
            angle = angle + 2
    while(angle < 270):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x*30, y*30)
            x = x + math.sin(2)
            y = y + math.cos(2)
            delay(0.01)
            angle = angle + 2
    while(angle < 360):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x*30, y*30)
            x = x + math.sin(2)
            y = y - math.cos(2)
            delay(0.01)
            angle = angle + 2     
close_canvas()
    
