import random

import numpy as np
import pygame

pygame.init()

<<<<<<< HEAD
# UPDATE THE GRID ACCORDING TO THE CONWAY'S GAME OF LIFE RULES.
=======

>>>>>>> ac5cf5b
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


# COUNT THE NUMBER OF ALIVE CELLS AROUND A PARTICULAR CELL.
def countNeighbours(currgen, i, j):
    sum = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            a = (i + a + gridx) % gridx
            b = (j + b + gridy) % gridy
            sum += currgen[a][b]
    sum -= currgen[i][j]
    return sum

# PYGAME WINDOW 
screen = pygame.display.set_mode((0, 0),pygame.RESIZABLE) # CREATE PYGAME WINDOW.
pygame.display.set_caption("Conway's Game Of Life") # SET THE WINDOWS NAME TO "Conway's Game Of Life".

<<<<<<< HEAD
# VARIABLES
width = 16 # CHANGES THE WIDTH OF THE CELLS.
upd = False # IF THIS IS TRUE ONLY THEN THE GIRD WILL UPDATE.
gridx = screen.get_width()//width # NUMBER OF COLUMNS.
gridy = screen.get_height()//width # NUMBER OF ROWS.
=======
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
>>>>>>> ac5cf5b

currgen = np.zeros((gridx, gridy)) # NUMPY 2 DIMENSIONAL ARRAY STORING CELLS STATE.

# INITIAL STATE (RANDOM 0s and 1s)
for i, j in np.ndindex(currgen.shape):
    currgen[i][j] = random.randint(0, 1)


tick = pygame.time.Clock()
run = True
# GAME LOOP
while run:
    pygame.display.flip()
    tick.tick(30) # SET THE FRAME RATE OF THE PYGAME WINDOW.
    screen.fill((24, 24, 24)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # ADD ALIVE CELL
        if pygame.mouse.get_pressed()[0]:
            mousepos = pygame.mouse.get_pos()
<<<<<<< HEAD
            i = mousepos[0]//width
            j = mousepos[1]//width
=======
            i = mousepos[0] // width
            j = mousepos[1] // width
>>>>>>> ac5cf5b
            currgen[i][j] = 1

        # ADD DEAD CELL
        if pygame.mouse.get_pressed()[2]:
            mousepos = pygame.mouse.get_pos()
<<<<<<< HEAD
            i = mousepos[0]//width
            j = mousepos[1]//width
=======
            i = mousepos[0] // width
            j = mousepos[1] // width
>>>>>>> ac5cf5b
            currgen[i][j] = 0
        if event.type == pygame.KEYDOWN:
            # STOP UPDATING
            if event.key == pygame.K_SPACE:
                upd = not upd
            # CLEAR THE GRID/MAKE ALL CELLS DEAD
            if event.key == pygame.K_r:
                upd = False
                currgen = np.zeros((gridx, gridy))

<<<<<<< HEAD
    # DRAWING PREVIOUS STATE
    for i in range(gridx):
        for j in range(gridy):
            if currgen[i][j]:
                prev_color = (160, 160, 160)
            else:
                prev_color = (0, 0, 0)
                
            pygame.draw.rect(screen, prev_color, (i*width + 1, j*width + 1, width-1, width-1), 3)

    # UPDATING
    if upd:        
        currgen = update(currgen, gridx, gridy)

    # DRAWING CURRENT STATE
    for i in range(gridx):
        for j in range(gridy):
            if currgen[i][j]:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, (i*width + 1, j*width + 1, width-1, width-1), 2)

    pygame.display.update() # UPDATE THE PYGAME WINDOW
=======
    drawGrid(screen, currgen, (128, 128, 128))

    if upd:
        currgen = update(currgen, gridx, gridy)

    drawGrid(screen, currgen, (255, 255, 255))

    pygame.display.update()
>>>>>>> ac5cf5b
