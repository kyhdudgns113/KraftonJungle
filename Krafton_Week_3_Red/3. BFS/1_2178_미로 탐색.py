from queue import Queue
import sys

sys.setrecursionlimit(10 ** 5)

n, m = map(int, sys.stdin.readline().split())
maze = list(list(sys.stdin.readline().strip()) for _ in range(n))
is_visit = list(list(False for _ in range(m)) for _ in range(n))


max_depth = 0


def bfs(row, col):
    global n, m, maze, is_visit, max_depth
    is_visit[row][col] = True
    depth = 1
    next_visit_queue = Queue()
    next_visit_queue.put([row, col, depth])

    while not next_visit_queue.empty():
        popped = next_visit_queue.get()
        now_row = popped[0]
        now_col = popped[1]
        if now_row == n - 1 and now_col == m - 1:
            max_depth = popped[2]
        next_depth = popped[2] + 1
        if now_row > 0 and not is_visit[now_row - 1][now_col] and maze[now_row - 1][now_col] == '1':
            is_visit[now_row - 1][now_col] = True
            next_visit_queue.put([now_row - 1, now_col, next_depth])
        if now_col > 0 and not is_visit[now_row][now_col - 1] and maze[now_row][now_col - 1] == '1':
            is_visit[now_row][now_col - 1] = True
            next_visit_queue.put([now_row, now_col - 1, next_depth])
        if now_row < n - 1 and not is_visit[now_row + 1][now_col] and maze[now_row + 1][now_col] == '1':
            is_visit[now_row + 1][now_col] = True
            next_visit_queue.put([now_row + 1, now_col, next_depth])
        if now_col < m - 1 and not is_visit[now_row][now_col + 1] and maze[now_row][now_col + 1] == '1':
            is_visit[now_row][now_col + 1] = True
            next_visit_queue.put([now_row, now_col + 1, next_depth])


bfs(0, 0)

print(max_depth)


