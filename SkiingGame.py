# Slalom Skiing Game
# Written by John Schindler johnwschindler4@yahoo.com

import pygame,sys,time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
backgroundColor = (255,255,255)
SURFACE = pygame.display.set_mode((300,700),0,32)
SURFACE.fill(backgroundColor)
myfont = pygame.font.SysFont("monospace",25)
pygame.display.set_caption('Slalom Skiing Game')

BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

# set up gates
pygame.draw.line(SURFACE, BLUE, (30,30), (50,30), 2)
pygame.draw.line(SURFACE, BLUE, (80,30), (100,30), 2)
pygame.draw.line(SURFACE, RED, (50,80), (70,80), 2)
pygame.draw.line(SURFACE, RED, (100,80), (120,80), 2)
pygame.draw.line(SURFACE, BLUE, (140,140), (160,140), 2)
pygame.draw.line(SURFACE, BLUE, (190,140), (210,140), 2)
pygame.draw.line(SURFACE, RED, (70,220), (90,220), 2)
pygame.draw.line(SURFACE, RED, (120,220), (140,220), 2)
pygame.draw.line(SURFACE, BLUE, (40,290), (60,290), 2)
pygame.draw.line(SURFACE, BLUE, (90,290), (110,290), 2)
pygame.draw.line(SURFACE, RED, (200,400), (220,400), 2)
pygame.draw.line(SURFACE, RED, (250,400), (270,400), 2)
pygame.draw.line(SURFACE, BLUE, (120,490), (140,490), 2)
pygame.draw.line(SURFACE, BLUE, (170,490), (190,490), 2)
pygame.draw.line(SURFACE, RED, (70,580), (90,580), 2)
pygame.draw.line(SURFACE, RED, (120,580), (140,580), 2)
pygame.draw.line(SURFACE, BLACK, (0,630), (300,630), 2)

skier = pygame.Rect(60, 5, 5, 5)

moveLeft = False
moveRight = False
moveDown = False
MOVESPEED = 4

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_DOWN:
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_DOWN:
                moveDown = False

    if moveDown and skier.top < 630:
        skier.top += MOVESPEED
    if moveLeft:
        skier.left -= MOVESPEED
    if moveRight:
        skier.right += MOVESPEED
    
    pygame.draw.rect(SURFACE, GREEN, skier)

    pygame.display.update()
    mainClock.tick(30)
