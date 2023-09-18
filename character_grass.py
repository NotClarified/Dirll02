from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
angle =270
while (1):
    while (x < 780): # 중앙시작, 우측하단 직선
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
    x = 780
    while (y < 540): # 우측하단 -> 우측상단 직선
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 5
        delay(0.01)
    y = 540
    
    while (x >20): # 우측상단 -> 좌측상단 직선
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 5
        delay(0.01)
    x = 20
    
    while (y >90): # 좌측상단 -> 좌측하단 직선
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 5
        delay(0.01)
    y = 90
    
    while (x < 400): # 좌측하단 -> 중앙 직선
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
        
    while(angle < 360 + 270): #270도가 6시 출발, 1바퀴 돌
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y+290)
        x = x + 200 * math.cos(math.radians(angle))
        y = y + 200 * math.sin(math.radians(angle))
        delay(0.01)
        angle = angle + 2
    angle = 0

close_canvas()
