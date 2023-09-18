from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
angle =270
while (1):
    while (x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
    x = 780
    while (y < 540):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 5
        delay(0.01)
    y = 540
    
    while (x >20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 5
        delay(0.01)
    x = 20
    
    while (y >90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 5
        delay(0.01)
    y = 90
    
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
        
    while(angle < 360 + 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y+200)
        x = x + 200 * math.cos(math.radians(angle))
        y = y + 200 * math.sin(math.radians(angle))
        delay(0.01)
        angle = angle + 2
    angle = 0
close_canvas()
    
