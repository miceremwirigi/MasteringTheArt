"""Conways game of life
 live cells with three or two neighbors stay alive
 dead cell with three live neighbors come to life
 everything else dies or stays dead
w
"""
import copy
import random
import sys
import time

width = 79
height = 20
ALIVE = '0'
DEAD = ' '

nextcells = {}  # dict to store the cell states

# generate random cells using random method
for y in range(height):
    for x in range(width):
        if random.randint(0, 1) == 1:
            nextcells[(x, y)] = ALIVE
        else:
            nextcells[(x, y)] = DEAD
        print(nextcells[(x, y)], end='')
    print("")
# cells = copy.deepcopy(nextcells)  # create a copy of the dict/array to check neighbors
while True:
    print("\n" * 10)  # separate each output
    cells = copy.deepcopy(nextcells)  # create a copy of the dict/array to check neighbors
    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end="")
        print("")

    for y in range(height):
        for x in range(width):
            # Set the neighbors
            # Wrap around the edges
            left = (x - 1) % width
            right = (x + 1) % width
            above = (y - 1) % height
            below = (y + 1) % height

            neighbors = 0
            # conditions to count the number of neighbors
            if cells[(left, above)] == ALIVE:
                neighbors += 1  # Top-left neighbor is ALIVE
            if cells[(x, above)] == ALIVE:
                neighbors += 1  # Top neighbor is ALIVE
            if cells[(right, above)] == ALIVE:
                neighbors += 1  # Top-right neighbor is ALIVE
            if cells[(left, y)] == ALIVE:
                neighbors += 1  # Left neighbor is ALIVE
            if cells[(right, y)] == ALIVE:
                neighbors += 1  # Right neighbor is ALIVE
            if cells[(left, below)] == ALIVE:
                neighbors += 1  # Bottom-left neighbor is ALIVE
            if cells[(x, below)] == ALIVE:
                neighbors += 1  # Bottom neighbor is ALIVE
            if cells[(right, below)] == ALIVE:
                neighbors += 1  # Bottom neighbor is ALIVE

            # print('Neigbors = {}'.format(neighbors))

            if cells[(x, y)] == ALIVE and (neighbors == 2 or neighbors == 3):
                # live cells with two or three neighbors stay alive
                nextcells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and neighbors == 3:
                # dead cells with three neighbors come to life
                nextcells[(x, y)] = ALIVE
            else:
                # everything else dies or stays dead
                nextcells[(x, y)] = DEAD
    try:
        time.sleep(1)  # Pause for one second before repeating
    except:
        print("Conway's Game of Life")
        sys.exit()  # end program once CTRL-C is pressed

"""for y in range (4):
    for x in range (3):
        print("{} ".format( random.randint(0,1)), end= " ")
    print("\n");

    #print("\n")
#print(type(nextcells))

"""
# print(nextcells)
