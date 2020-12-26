from collections import Counter
from utils import digits

def satisfy(x):
    p = digits(x)
    for i, dig in enumerate(p[:-1]):
        if dig > p[i + 1]:
            return False
    return any(q == w for q, w in zip(p, p[1:]))


def satisfy_p2(x):
    p = digits(x)
    for i, dig in enumerate(p[:-1]):
        if dig > p[i + 1]:
            return False
    return any(a == 2 for a in Counter(p).values())

print(len([x for x in range(197487, 673251+1) if satisfy(x)]))
print(len([x for x in range(197487, 673251+1) if satisfy_p2(x)]))