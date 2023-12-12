import pygame
import math, sys, os
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 720, 480
screen = pygame.display.set_mode((w, h))
running = True

module = sys.modules['__main__']
path, name = os.path.split(module.__file__)
path = os.path.join(path, 'ak.png')

img0 = pygame.image.load(path)
img0.convert()

rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

center = w//2, h//2
img = img0
rect = img.get_rect()
rect.center = center

angle = 0
scale = 1

mouse = pygame.mouse.get_pos()

speed = 5
x_pos = w//2
y_pos = h//2
x_change = 0
y_change = 0
flipped = False

gravity = 0.5

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)

            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)

            elif event.key == K_o:
                img = img0
                angle = 0
                scale = 1

            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
                flipped = not flipped
            
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)

            elif event.key == K_l:
                img = pygame.transform.laplacian(img)

            elif event.key == K_2:
                img = pygame.transform.scale2x(img)

            rect = img.get_rect()
            rect.center = center

        elif event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            d = math.sqrt(x ** 2 + y ** 2)

            angle = math.degrees(-math.atan2(y, x))
            img = pygame.transform.rotozoom(img0, angle, scale)
            rect = img.get_rect()
            rect.center = center
    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x_change = -speed
        if not flipped:
            img = pygame.transform.flip(img, True, False)
            flipped = True
    elif keys[K_RIGHT]:
        x_change = speed
        if flipped:
            img = pygame.transform.flip(img, True, False)
            flipped = False
    else:
        x_change = 0

    if keys[K_UP]:
        y_change = -speed
    elif keys[K_DOWN]:
        y_change = speed
    else:
        y_change = 0

    y_change += gravity

    x_pos += x_change
    y_pos += y_change

    rect = img.get_rect()
    rect.center = (x_pos, y_pos)

    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()