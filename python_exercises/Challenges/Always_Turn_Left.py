import sys
import random
import requests
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

NORTH, SOUTH, WEST, EAST = [2**i for i in range(4)]
OFFSETS     =  {NORTH: (0 ,-1),
                SOUTH: (0 , 1),
                WEST:  (-1, 0),
                EAST:  (1,  0)
                }
OPPOSITES   =  {NORTH: SOUTH,
                SOUTH: NORTH,
                EAST: WEST,
                WEST: EAST
                }
LEFTS       =  {NORTH: WEST,
                SOUTH: EAST,
                WEST: SOUTH,
                EAST: NORTH
                }
RIGHTS      =  {NORTH: EAST,
                SOUTH: WEST,
                WEST: NORTH,
                EAST: SOUTH
                }
def maze(entrance_to_exit, exit_to_entrance):
    maze = defaultdict(int)
    x,y=0,-1
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
                raise RuntimeError('unexpected char % in input.' %c)
        direction = OPPOSITES[direction]
        del maze[(x,y)]
    xs = sorted(set(x for x, _ in maze.iterkeys()))
    ys = sorted(set(y for _, y in maze.iterkeys()))
    return "\n".join("".join("%x" % maze[x, y] for x in xs) for y in ys)

def main():
    f = sys.argv[1]
    open_file = open(f,'r')
    lines = open_file.readlines()
    first_line = lines.pop(0)
    write_file = open(f+'output.in','w')
    i = 0
    for line in lines:
        result = maze(line.strip().split(' ')[0], line.strip().split(' ')[1])
        write_file.write('Case #'+str(i+1)+':\n')
        write_file.write(result+'\n')
        i+=1

if __name__ == '__main__':
    main()