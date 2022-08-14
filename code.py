import pygame
import time
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((450,720))
clock = pygame.time.Clock()
p_index = 0
planet_l = ["Pic1.png", "Pic2.png", "Pic3.png"]

bg_img = pygame.image.load('Bg1.png')
bg_img = pygame.transform.scale(bg_img,(450,720))
planet = pygame.image.load(planet_l[p_index])
planet = pygame.transform.scale(planet,(150,150))
ship = pygame.image.load('ship.png')
ship = pygame.transform.scale(ship,(130,100))
b_img = pygame.image.load('bullet.png')
b_img = pygame.transform.scale(b_img,(20,45))
win_img = pygame.image.load('win.png')
win_img = pygame.transform.scale(win_img,(400,300))

planet_x = 150
move_direction = 'right'
fired = False
bullet_y = 625

alive = False
runing = True
while runing:
    window.blit(bg_img,(0,0))
    window.blit(planet, [planet_x, 50])
    window.blit(b_img, [205, bullet_y])
    window.blit(ship,(150, 600))
    if bullet_y < 125 and planet_x > 100 and planet_x < 200:
        p_index += 1
        if (p_index < len(planet_l)):
            planet = pygame.image.load(planet_l[p_index])
            planet = pygame.transform.scale(planet,(150,150))
            planet_x = 10
        else:
            print("YOU WIN!!!")
            alive  = True
        fired = False
        bullet_y = 625

    if alive == False:
        pygame.display.update()
        clock.tick(120)
        if move_direction == 'right':
           planet_x = planet_x + 1
           if planet_x == 300:
               move_direction = 'left'
        else:
           planet_x = planet_x - 1
           if planet_x == 0:
               move_direction = 'right'
               
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == True:
            fired = True
        if fired is True:
            bullet_y = bullet_y - 5
            if bullet_y == 50:
                fired = False
                bullet_y = 625
    else:
        window.blit(win_img,(10, 200))
                
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
    
