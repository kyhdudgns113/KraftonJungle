import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

col = [0]
row = [0]

for _ in range(n):
    gase, position = map(int, sys.stdin.readline().split())

    if gase == 1:
        col.append(position)
    else:
        row.append(position)

row.append(h)
col.append(w)

row.sort()
col.sort()

rmax = 0
cmax = 0

for i in range(len(row) - 1):
    rmax = max(rmax, row[i+1] - row[i])

for i in range(len(col) - 1):
    cmax = max(cmax, col[i+1] - col[i])

print(rmax * cmax)