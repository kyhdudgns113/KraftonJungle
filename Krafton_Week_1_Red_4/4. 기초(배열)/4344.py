import sys

c = int(sys.stdin.readline())

for _ in range(c):
    inp = list(map(int, sys.stdin.readline().split()))
    n = inp.pop(0)
    avg = sum(inp) / len(inp)
    mem = 0
    for score in inp:
        if score > avg:
            mem += 1
    sys.stdout.write("%.3f%%\n" % (float(mem)*100/len(inp)))
