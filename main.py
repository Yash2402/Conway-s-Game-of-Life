import random

import numpy as np
import pygame

pygame.init()


def update(currgen, gridx, gridy):
    next = np.zeros((gridx, gridy))
    for i in range(gridx):
        for j in range(gridy):
            state = currgen[i][j]
            aliveneigh = countNeighbours(currgen, i, j)
            if state == 0 and aliveneigh == 3:
                next[i][j] = 1
            elif state == 1 and (aliveneigh < 2 or aliveneigh > 3):
                next[i][j] = 0
            else:
                next[i][j] = state
    return next


def countNeighbours(currgen, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            a = (x + i + gridx) % gridx
            b = (y + j + gridy) % gridy
            sum += currgen[a][b]
    sum -= currgen[x][y]
    return sum


def drawGrid(screen, currgen, color):
    for i in range(gridx):
        for j in range(gridy):
            if currgen[i][j]:
                pygame.draw.rect(
                    screen,
                    color,
                    (i * width + 1, j * width + 1, width - 1, width - 1),
                    width=2,
                )
            else:
                pygame.draw.rect(
                    screen,
                    (0, 0, 0),
                    (i * width + 1, j * width + 1, width - 1, width - 1),
                    width=2,
                )


screen = pygame.display.set_mode((1024, 1024), pygame.RESIZABLE)
pygame.display.set_caption("Conway's Game Of Life")
width = 16
gridx = screen.get_width() // width
gridy = screen.get_height() // width

run = True
currgen = np.zeros((gridx, gridy))
for i, j in np.ndindex(currgen.shape):
    currgen[i][j] = random.randint(0, 1)
upd = False
tick = pygame.time.Clock()

while run:
    pygame.display.flip()
    tick.tick(120)
    screen.fill((24, 24, 24))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            mousepos = pygame.mouse.get_pos()
            i = mousepos[0] // width
            j = mousepos[1] // width
            currgen[i][j] = 1
        if pygame.mouse.get_pressed()[2]:
            mousepos = pygame.mouse.get_pos()
            i = mousepos[0] // width
            j = mousepos[1] // width
            currgen[i][j] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                upd = not upd
            if event.key == pygame.K_r:
                upd = False
                currgen = np.zeros((gridx, gridy))

    drawGrid(screen, currgen, (128, 128, 128))

    if upd:
        currgen = update(currgen, gridx, gridy)

    drawGrid(screen, currgen, (255, 255, 255))

    pygame.display.update()
