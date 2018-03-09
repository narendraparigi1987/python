from collections import defaultdict
import sys

NORTH, SOUTH, WEST, EAST = [2 ** i for i in range(4)]
OFFSETS = {
	NORTH: ( 0, -1),
	SOUTH: ( 0,  1),
	WEST:  (-1,  0),
	EAST:  ( 1,  0),
}
OPPOSITES = {
	NORTH: SOUTH,
	SOUTH: NORTH,
	WEST:  EAST,
	EAST:  WEST,
}
LEFTS = {
	NORTH: WEST,
	WEST:  SOUTH,
	SOUTH: EAST,
	EAST:  NORTH,
}
RIGHTS = {
	NORTH: EAST,
	EAST:  SOUTH,
	SOUTH: WEST,
	WEST:  NORTH,
}


def maze(entrance_to_exit, exit_to_entrance):
	maze = defaultdict(int)
	x, y = 0, -1
	direction = SOUTH
	for path in [entrance_to_exit, exit_to_entrance]:
		for c in path:
			if c == "W":
				dx, dy = OFFSETS[direction]
				x += dx
				y += dy
				maze[x, y] |= OPPOSITES[direction]
			elif c == "L":
				direction = LEFTS[direction]
			elif c == "R":
				direction = RIGHTS[direction]
			else:
				raise RuntimeError("unexpected char '%s' in input." % c)
		direction = OPPOSITES[direction]
		del maze[(x, y)]
	xs = sorted(set(x for x, _ in maze.iterkeys()))
	ys = sorted(set(y for _, y in maze.iterkeys()))
	return "\n".join("".join("%x" % maze[x, y] for x in xs) for y in ys)

N = sys.argv[1:]
#for X in range(N):
#print "Case #%s:" % (X+1)
print maze(N[0],N[1])