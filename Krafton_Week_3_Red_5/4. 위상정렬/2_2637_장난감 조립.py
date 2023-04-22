from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

connection_list = list([] for _ in range(n + 1))
how_many = list(list(0 for _ in range(n + 1)) for _ in range(n + 1))
used_elements = list(list(0 for _ in range(n + 1)) for _ in range(n + 1))
fathers = list(0 for _ in range(n + 1))

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    connection_list[x].append(y)
    how_many[x][y] = k
    fathers[y] += 1

###############################
#
#   topology_list 만들기
#
###############################
topology_list = []
visit_queue = deque()
root = 0
for i in range(1, n + 1):
    if fathers[i] == 0:
        visit_queue.append(i)
        root = i

while len(visit_queue) > 0:
    now = visit_queue.popleft()
    topology_list.append(now)
    for next_node in connection_list[now]:
        fathers[next_node] -= 1
        if fathers[next_node] == 0:
            visit_queue.append(next_node)


for i in range(n - 1, -1, -1):
    new_i = topology_list[i]
    # print(f'\n{new_i}')
    if len(connection_list[new_i]) == 0:
        used_elements[new_i][new_i] = 1
    else:
        for element in connection_list[new_i]:
            for j in range(1, n + 1):
                used_elements[new_i][j] += how_many[new_i][element] * used_elements[element][j]
                # print(f'    ({element}, {j}) = {how_many[new_i][element]}, {used_elements[element][j]}')
    # print(used_elements[new_i])

for i in range(1, n + 1):
    if used_elements[root][i] > 0:
        sys.stdout.write(f'{i} {used_elements[root][i]}\n')












