f = [int(x)  for x in open("input.txt").read().strip().split(",")]
# f = [2,4,4,5,99,0]


f[1] = 82

f[2] = 50
i = 0

while f[i] != 99:
    if f[i] == 1:
        a, b, c = f[i+1:i+4]
        f[c] = f[a] + f[b]
        i += 4
    elif f[i] == 2:
        a, b, c = f[i+1:i+4]
        f[c] = f[a] * f[b]
        i += 4
    else:
        print("something wrong")
    # print(f, "i: ", i)
print(f[0])

print(100 * 82 + 50)