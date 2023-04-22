import sys

sys.setrecursionlimit(10 ** 5)


def dfs(row, col):  # 2가지 경우로 나뉘는걸 체크해주기 위한 함수.
    for k in range(4):
        nx = dx[k] + row
        ny = dy[k] + col
        if 0 <= nx < n and 0 <= ny < m and is_visit[nx][ny]:
            is_visit[nx][ny] = False
            if matrix[nx][ny] != 0:
                dfs(nx, ny)


input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
is_visit = [[False] * m for _ in range(n)]  # 방문 체크
t = 0


def one_year():
    for row in range(n):
        for col in range(m):
            if matrix[row][col] != 0:
                is_visit[row][col] = True
                c = matrix[row][col]
                for k in range(4):
                    nx = dx[k] + row
                    ny = dy[k] + col
                    if 0 <= nx < n and 0 <= ny < m and not is_visit[nx][ny]:
                        if matrix[nx][ny] == 0:
                            c -= 1
                            if c == 0:
                                break
                matrix[row][col] = c


while True:
    t += 1
    one_year()
    ch = 0
    for row in range(n):
        for col in range(m):
            if matrix[row][col] != 0 and is_visit[row][col]:
                dfs(row, col)
                ch += 1
            elif matrix[row][col] == 0 and is_visit[row][col]:
                is_visit[row][col] = False

    if ch >= 2:
        print(t)
        exit()
    elif ch == 0:
        print(0)
        exit()