import sys

n = int(sys.stdin.readline())

hansu = 0

for i in range(1, n+1):
    case_su = list(str(i))

    if len(case_su) < 3:
        hansu += 1
        continue

    first = int(case_su[0])
    second = int(case_su[1])
    dif = second - first
    isHansu = 1

    for j, su in enumerate(case_su):
        if j < 2:
            continue
        first = second
        second = int(case_su[j])
        if second-first != dif:
            isHansu = 0
            break
    hansu += isHansu

print(hansu)