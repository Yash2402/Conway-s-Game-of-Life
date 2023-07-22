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


screen = pygame.display.set_mode((1024, 1024),pygame.RESIZABLE)
pygame.display.set_caption("Conway's Game Of Life")
radius = 8
gridx = int(((screen.get_width()/(2*radius))/2)*2)
gridy = int(((screen.get_height()/(2*radius))/2)*2)

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
            i = int(mousepos[0]/(2*radius))
            j = int(mousepos[1]/(2*radius))
            currgen[i][j] = 1
        if pygame.mouse.get_pressed()[2]:
            mousepos = pygame.mouse.get_pos()
            i = int(mousepos[0]/(2*radius))
            j = int(mousepos[1]/(2*radius))
            currgen[i][j] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                upd = not upd
            if event.key == pygame.K_r:
                upd = False
                currgen = np.zeros((gridx, gridy))
    
    if upd:        
        currgen = update(currgen, gridx, gridy)
    for i in range(gridx):
        for j in range(gridy):
            if currgen[i][j]:
                color1 = (255, 255, 255)
                color2 = (255, 0, 0)
            else:
                color1 = (0, 0, 0)
                color2 = (0, 0, 0)
            pygame.draw.rect(screen, color1, (i*2*radius + 1, j*2*radius + 1, 2*radius-1, 2*radius-1), width=2)
            # pygame.draw.circle(screen, color, (i*2*radius + radius + 1, j*2*radius + radius + 1), radius)

    pygame.display.update()


