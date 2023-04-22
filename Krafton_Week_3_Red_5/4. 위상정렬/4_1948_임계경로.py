from queue import Queue
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

connection_list = list([] for _ in range(n + 1))
num_parent = list(0 for _ in range(n + 1))

for _ in range(m):
    node_start, node_end, cost = map(int, sys.stdin.readline().split())
    connection_list[node_start].append([node_end, cost])
    num_parent[node_end] += 1

start, end = map(int, sys.stdin.readline().split())

max_cost_list = list(0 for _ in range(n + 1))
path_dict_list = list(dict() for _ in range(n + 1))
visit_queue = Queue()
visit_queue.put(start)


while not visit_queue.empty():
    now_node = visit_queue.get()
    now_cost = max_cost_list[now_node]

    if connection_list[now_node]:
        for next_node, next_cost in connection_list[now_node]:

            ##################################################
            #   cost 가 최대치보다 크면 path 리스트를 갱신해준다.  #
            #   cost 가 최대치랑 같으면 path 리스트를 추가해준다.  #
            #   cost 가 최대치보다 작으면 아무것도 안한다.         #
            ##################################################
            if now_cost + next_cost >= max_cost_list[next_node]:
                if now_cost + next_cost > max_cost_list[next_node]:
                    path_dict_list[next_node] = path_dict_list[now_node].copy()
                    max_cost_list[next_node] = now_cost + next_cost
                else:
                    for key in path_dict_list[now_node].keys():
                        path_dict_list[next_node][key] = 1

                path_dict_list[next_node][(now_node, next_node)] = 1

            num_parent[next_node] -= 1
            if not num_parent[next_node]:
                visit_queue.put(next_node)

    #   안하면 메모리 초과 나온다.
    if now_node != end:
        path_dict_list[now_node].clear()

print(max_cost_list[end])
print(len(path_dict_list[end]))


