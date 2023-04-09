import sys


dwarf = list(int(sys.stdin.readline()) for i in range(9))
dwarf.sort()

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarf[k])
            exit()

