import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 240))
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

running = True

points = []
drawing = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if len(points) > 0:
                    points.pop()
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            points[-1] = event.pos
        screen.fill(WHITE)
        if len(points)>1:
            rect = pygame.draw.lines(screen, BLUE, True, points, 3)
            pygame.draw.rect(screen, GREEN, rect, 1)
        pygame.display.update()

pygame.quit()