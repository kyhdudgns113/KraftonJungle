from queue import Queue
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

connected_list = list([] for _ in range(n + 1))

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    connected_list[a].append(b)
    connected_list[b].append(a)


hasParent = list(0 for _ in range(n + 1))
hasParent[1] = 1


def bfs(root):
    global hasParent

    will_visit_queue = Queue()
    will_visit_queue.put(root)

    while not will_visit_queue.empty():
        parent = will_visit_queue.get()
        for son in connected_list[parent]:
            if not hasParent[son]:
                hasParent[son] = parent
                will_visit_queue.put(son)

bfs(1)

for i in range(2, n + 1):
    print(hasParent[i])




