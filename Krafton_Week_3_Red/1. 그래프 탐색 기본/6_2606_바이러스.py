import sys

num_computers = int(sys.stdin.readline())
num_connections = int(sys.stdin.readline())

isConnected = list(list(0 for _ in range(num_computers + 1)) for _ in range(num_computers + 1))

for _ in range(num_connections):
    c1, c2 = map(int, sys.stdin.readline().split())
    isConnected[c1][c2] = 1
    isConnected[c2][c1] = 1


isVisited = list(0 for _ in range(num_computers + 1))
virused = -1


def dfs(now):
    global isVisited, isConnected, num_computers, virused
    isVisited[now] = 1
    virused += 1

    for next_v in range(num_computers + 1):
        if isVisited[next_v] == 0 and isConnected[now][next_v] == 1:
            dfs(next_v)


dfs(1)
print(virused)
