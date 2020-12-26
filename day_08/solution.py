# import copy
from utils import readfile
# import numpy as np
from collections import Counter
f = readfile
width = 25
height = 6
a = str(f[0])
# # a = "0222112222120000"

# layers = []
layers = [a[i: i + width * height] for i in range(0, len(a), width * height)]
counters = [Counter(l) for l in layers]
counters = [Counter(layer) for layer in layers]

c = min(counters, key=lambda x: x['0'])
print(f'part 1: {c["1"] * c["2"]}')

img = layers[0]
for layer in layers[1:]:
    img = [layer[p] if img[p] == '2' else img[p] for p in range(width * height)]

print('part 2:')
for r in range(height):
    print(''.join(img[r * width:(r + 1) * width]).replace('0', ' ').replace('1', 'x'))