import sys

n = int(sys.stdin.readline())

tree = {}

for _ in range(n):
    p, l, r = map(str, sys.stdin.readline().split())
    tree[p] = [l, r]


def vlr(here_node):
    global tree

    sys.stdout.write(here_node)

    if tree[here_node][0] != '.':
        vlr(tree[here_node][0])
    if tree[here_node][1] != '.':
        vlr(tree[here_node][1])


def lvr(here_node):
    global tree

    if tree[here_node][0] != '.':
        lvr(tree[here_node][0])

    sys.stdout.write(here_node)

    if tree[here_node][1] != '.':
        lvr(tree[here_node][1])


def lrv(here_node):

    if tree[here_node][0] != '.':
        lrv(tree[here_node][0])
    if tree[here_node][1] != '.':
        lrv(tree[here_node][1])
    sys.stdout.write(here_node)


vlr('A')
print()
lvr('A')
print()
lrv('A')
