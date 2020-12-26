class Node:
    def __init__(self, val, parent=None):
        self.name = val
        self.children = []
        self.parent = parent
    def __repr__(self):
        asdf = []
        for c in self.children:
            asdf.append(c.name)
        return f"({self.name}, {asdf})"
node_lookup = {}


f = open('input.txt').read().strip().split("\n")


for line in f:
    l, r = line.split(")")

    if l in node_lookup:
        if r in node_lookup:
            node_lookup[l].children.append(node_lookup[r])
            node_lookup[r].parent = node_lookup[l]
        else:
            newNode = Node(r, node_lookup[l])
            node_lookup[r] = newNode
            node_lookup[l].children.append(newNode)
    else:
        newNode = Node(l)
        node_lookup[l] = newNode
        if r in node_lookup:
            node_lookup[l].children.append(node_lookup[r])
            node_lookup[r].parent = node_lookup[l]
        else:
            newNode = Node(r, node_lookup[l])
            node_lookup[r] = newNode
            node_lookup[l].children.append(newNode) 
root = node_lookup["COM"]

q = [root]

def height(node):
    if node is None:
        return 0
    else:
        heights = [height(c) for c in node.children]
        if len(heights) == 0:
            return 1
        return max(heights) + 1


nodes_and_depths = []
def printGivenLevel(r, level, depth):
    if r is None:
        return
    if level == 1:
        nodes_and_depths.append((r.name, depth))
    elif level > 1:
        for c in r.children:
            printGivenLevel(c, level - 1, depth + 1)


def printLevelOrder(r):
    h = height(r)
    for i in range(1, h + 1):
        printGivenLevel(r, i, 0)


printLevelOrder(root)

print(sum(x[1] for x in nodes_and_depths))
you = node_lookup["YOU"]
san = node_lookup["SAN"]

def dist(root, n1, n2):
    def distUtil(n1, n2):
        q = [(n1, [])]
        seen = set()
        seen.add(n1)
        while q:
            curr, path = q.pop(0)
            if curr == n2:
                return path + [n2]
            neighbors = curr.children + [curr.parent]
            for n in neighbors:
                if n and n not in seen:
                    seen.add(n)
                    q.append((n, path + [curr]))
        return []
    path = distUtil(n1, n2)[1:-1]
    return len(path) - 1 if path else 0

print(dist(root, you, san))
