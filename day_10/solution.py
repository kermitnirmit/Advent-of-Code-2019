from collections import defaultdict, deque
import math
f = [x for x in open("input.txt").read().splitlines()]


ast = set()
for i, line in enumerate(f):
    for j, c in enumerate(line):
        print(i, j, c)
        if c == "#":
            ast.add((i, j))

print(ast)

from itertools import combinations

c = defaultdict(int)
c2 = defaultdict(list)



def find_can_see(a, b):
    dy = b[0] - a[0]
    dx = b[1] - a[1]
    
    # Check all integer points between a and b
    blocked = False
    min_x = min(a[1], b[1])
    max_x = max(a[1], b[1])
    min_y = min(a[0], b[0])
    max_y = max(a[0], b[0])
    
    # Handle vertical lines
    if dx == 0:
        for y in range(min_y + 1, max_y):
            if (y, a[1]) in ast:
                blocked = True
                break
    # Handle horizontal lines        
    elif dy == 0:
        for x in range(min_x + 1, max_x):
            if (a[0], x) in ast:
                blocked = True
                break
    else:
        # Get GCD to find step size for integer points
        from math import gcd
        step = gcd(abs(dx), abs(dy))
        dx //= step
        dy //= step
        
        # Check each integer point along the line
        curr = (a[0] + dy, a[1] + dx)
        while curr != b:
            if curr in ast:
                blocked = True
                break
            curr = (curr[0] + dy, curr[1] + dx)
    
    if not blocked:
        return True
    return False








for a, b in combinations(ast, 2):
    # Get slope between points
    if find_can_see(a, b):
        c[a] += 1
        c2[a].append(b)
        c[b] += 1
        c2[b].append(a)
    
max_v = max(c.values())
print(max_v)


monitoring_station = max(c, key=lambda x: c[x])
print(monitoring_station)
print(len(c2[monitoring_station]))

q = c2[monitoring_station]


def find_angle(a, b):
    dy = b[0] - a[0]
    dx = b[1] - a[1]
    
    # Calculate angle using atan2, adjusted for the specified orientation
    angle = math.atan2(-dx, dy)  # -dx because 0 degrees is along the positive y-axis
    angle_deg = math.degrees(angle)
    normalize = (angle_deg + 180) % 360
    
    # Normalize to [0, 360)
    
    return normalize

print(find_angle((0, 0), (-1, 0)))
print(find_angle((0, 0), (0, 1)))
print(find_angle((0, 0), (1, 0)))
print(find_angle((0, 0), (0, -1)))


# while q:
q.sort(key=lambda x: find_angle(monitoring_station, x))
print(q)

q = deque(q) 
count = 0
found = False
while not found:
    while q:
        a = q.popleft()
        ast.remove(a)
        count += 1
        if count == 200:
            print(a[1] * 100 + a[0])
            found = True
            break
    if not q:
        new_connections = [x for x in ast if find_can_see(monitoring_station, x)]
        new_connections.sort(key=lambda x: find_angle(monitoring_station, x))
        q = deque(new_connections)
