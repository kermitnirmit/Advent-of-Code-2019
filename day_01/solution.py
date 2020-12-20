f = open("input.txt").read().strip().split("\n")

a = sum([int(x) // 3 - 2 for x in f])
print(a)


b = [int(x) for x in f]
# b = [100756]
c = 0
for i in range(len(b)):
    while b[i] > 6:
        b[i] = b[i] // 3 - 2
        # print(b[i])
        c += b[i]
print(c)
