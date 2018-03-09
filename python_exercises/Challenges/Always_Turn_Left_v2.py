import sys
import random
import requests
from bs4 import BeautifulSoup
from collections import Counter, defaultdict
import json
import time

NORTH,SOUTH,WEST,EAST = [2**i for i in range(4)]

OFFSETS =   {
                NORTH: (0,-1),
                SOUTH: (0,1),
                WEST:  (-1,0),
                EAST:  (1,0),
            }

OPPOSITES = {
                NORTH: SOUTH,
                SOUTH: NORTH,
                WEST:  EAST,
                EAST:  WEST
            }

RIGHTS =    {
                NORTH: EAST,
                EAST:  SOUTH,
                SOUTH: WEST,
                WEST:  NORTH
            }
LEFTS =     {
                NORTH: WEST,
                WEST:  SOUTH,
                SOUTH: EAST,
                EAST:  NORTH
            }

def maze(entrance_to_exit, exit_to_entrance):
    x,y = 0,-1
    maze=defaultdict(int)
    direction = SOUTH
    for path in [entrance_to_exit,exit_to_entrance]:
        for c in path:
            if c == 'W':
                dx,dy = OFFSETS[direction]
                x+=dx
                y+=dy
                maze[x,y] |= OPPOSITES[direction]
            elif c == 'R':
                direction = RIGHTS[direction]
            elif c == 'L':
                direction = LEFTS[direction]
            else:
                raise RuntimeError('Unexpected char %s in input.'%c)
        direction = OPPOSITES[direction]
        del maze[(x,y)]
    
    xs = sorted(set(x for x, _ in maze.iterkeys()))
    ys = sorted(set(y for _, y in maze.iterkeys()))

    return "\n".join("".join('%x' % maze[x,y] for x in xs) for y in ys)

def main():
    f = sys.argv[1]
    open_file = open(f,'r')
    lines = open_file.readlines()
    first_line = lines.pop(0)
    write_file = open(f+'output_v2.in','w')
    i=0
    for line in lines:
        write_file.write('Case #'+str(i+1)+':\n')
        result = maze(line.strip().split(' ')[0], line.strip().split(' ')[1])
        write_file.write(result+'\n')
        i+=1

if __name__ == '__main__':
    main()