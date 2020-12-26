from collections import defaultdict
from utils import dirs_2d_4
f = open('input.txt').read().strip().split("\n")

mapping = dict(zip(["U", "R", "D", "L"], dirs_2d_4))

line_1_points = set()
common_points = set()

insts = f[0].split(",")
x, y = 0,0

steps_0 = defaultdict(int)
c = 0
for inst in insts:
    d = inst[0]
    dist = int(inst[1:])
    dx, dy = mapping[d]
    for i in range(dist):
        c+=1
        x += dx
        y += dy
        line_1_points.add((x,y))
        steps_0[(x,y)] = c

insts = f[1].split(",")
x,y = 0,0
steps_1 = defaultdict(int)
c = 0
for inst in insts:
    d = inst[0]
    dist = int(inst[1:])
    dx, dy = mapping[d]
    for i in range(dist):
        c += 1
        x += dx
        y += dy
        if (x,y) in line_1_points:
            common_points.add((x,y))
            steps_1[(x,y)] = c

print(min(abs(x) + abs(y) for x,y in common_points))

print(min(steps_0[point] + steps_1[point] for point in common_points))