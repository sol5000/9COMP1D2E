import pygame
from pygame.locals import *

size = 1000,800
width, height = size
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("c.png")
rect = ball.get_rect()
speed = [2, 2]

while running:
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(RED)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(ball, rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()