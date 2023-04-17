from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())

matrix = list(list(sys.stdin.readline().strip()) for _ in range(n))
min_depth = list(list(0x7fffffff for _ in range(n)) for _ in range(n))
is_visit = list(list(False for _ in range(n)) for _ in range(n))

pq = [[1, 0, 0, 0]]

min_depth[0][0] = 0

while len(pq) > 0:
    one_is_white, depth, row, col = heappop(pq)
    if row > 0 and matrix[row - 1][col] == '1' and depth < min_depth[row - 1][col]:
        min_depth[row - 1][col] = depth
        heappush(pq, [1, depth, row - 1, col])
    if row > 0 and matrix[row - 1][col] == '0' and depth + 1 < min_depth[row - 1][col]:
        min_depth[row - 1][col] = depth + 1
        heappush(pq, [2, depth + 1, row - 1, col])

    if col > 0 and matrix[row][col - 1] == '1' and depth < min_depth[row][col - 1]:
        min_depth[row][col - 1] = depth
        heappush(pq, [1, depth, row, col - 1])
    if col > 0 and matrix[row][col - 1] == '0' and depth + 1 < min_depth[row][col - 1]:
        min_depth[row][col - 1] = depth + 1
        heappush(pq, [2, depth + 1, row, col - 1])

    if row < n - 1 and matrix[row + 1][col] == '1' and depth < min_depth[row + 1][col]:
        min_depth[row + 1][col] = depth
        heappush(pq, [1, depth, row + 1, col])
    if row < n - 1 and matrix[row + 1][col] == '0' and depth + 1 < min_depth[row + 1][col]:
        min_depth[row + 1][col] = depth + 1
        heappush(pq, [2, depth + 1, row + 1, col])

    if col < n - 1 and matrix[row][col + 1] == '1' and depth < min_depth[row][col + 1]:
        min_depth[row][col + 1] = depth
        heappush(pq, [1, depth, row, col + 1])
    if col < n - 1 and matrix[row][col + 1] == '0' and depth + 1 < min_depth[row][col + 1]:
        min_depth[row][col + 1] = depth + 1
        heappush(pq, [2, depth + 1, row, col + 1])

print(min_depth[n - 1][n - 1])