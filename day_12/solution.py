from collections import defaultdict, deque
import math
from utils import ints
import itertools
f = [x for x in open("input.txt").read().splitlines()]

q = []
for line in f:
    q.append(ints(line) + [0,0,0])
def lcm(a, b):
    return (a * b) // math.gcd(a, b)
print(q)
sets = [set((q[0])), set((q[1])), set((q[2])), set((q[3]))]
cycles = [0,0,0,0]
for i in range(1000):
    next_q = []
    q_index = list(range(len(q)))
    # for qidx in q_index:
    #     if tuple(q[qidx]) in sets[qidx]:
    #         cycles[qidx] = i
    #         print(cycles)
    #         # if all (x > 0 for x in cycles):
    #         #     break
    #     else:
    #         sets[qidx].add(tuple(q[qidx]))
    # if all (x > 0 for x in cycles):
    #     break
    for a,b in itertools.combinations(q_index, 2):
        if q[a][0] < q[b][0]:
            q[a][3] += 1
            q[b][3] -= 1
        elif q[a][0] > q[b][0]:
            q[a][3] -= 1
            q[b][3] += 1
        if q[a][1] < q[b][1]:
            q[a][4] += 1
            q[b][4] -= 1
        elif q[a][1] > q[b][1]:
            q[a][4] -= 1
            q[b][4] += 1
        if q[a][2] < q[b][2]:
            q[a][5] += 1
            q[b][5] -= 1
        elif q[a][2] > q[b][2]:
            q[a][5] -= 1
            q[b][5] += 1
    for idx, a in enumerate(q):
        next_q.append([a[0] + a[3], a[1] + a[4], a[2] + a[5], a[3], a[4], a[5]])
    q = next_q
# print(q)
# print(cycles)
# l_val = 1
# for i in cycles:
#     l_val = lcm(l_val, i)
# print(l_val)
p1 = 0 
for a in q:
    p1 += sum(abs(x) for x in a[:3]) * sum(abs(x) for x in  a[3:])
print(p1)
