import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

area = list(list(map(int, sys.stdin.readline().split())) for i in range(n))
isVisit = list(list(0 for _ in range(n)) for __ in range(n))

result = 0


def dfs(height, row, col):
    global area, isVisit, n

    isVisit[row][col] = 1

    if col > 0 and isVisit[row][col - 1] == 0 and area[row][col - 1] > height:
        dfs(height, row, col - 1)
    if row > 0 and isVisit[row - 1][col] == 0 and area[row - 1][col] > height:
        dfs(height, row - 1, col)
    if col + 1 < n and isVisit[row][col + 1] == 0 and area[row][col + 1] > height:
        dfs(height, row, col + 1)
    if row + 1 < n and isVisit[row + 1][col] == 0 and area[row + 1][col] > height:
        dfs(height, row + 1, col)


for height in range(101):
    isVisit = list(list(0 for _ in range(n)) for __ in range(n))
    temp_result = 0
    for row in range(n):
        for col in range(n):
            if isVisit[row][col] == 0 and area[row][col] > height:
                temp_result += 1
                dfs(height, row, col)

    result = max(result, temp_result)

print(result)
