from queue import Queue
import sys

r, c = map(int, sys.stdin.readline().split())

titup = list(list(sys.stdin.readline().strip()) for _ in range(r))

dived_times = list(list(0x7fffffff for _ in range(c)) for _ in range(r))
dived_queue = Queue()
visit_times = list(list(0x7fffffff for _ in range(c)) for _ in range(r))
visit_queue = Queue()
dest_row = 0
dest_col = 0

for row in range(r):
    for col in range(c):
        if titup[row][col] == '*':
            dived_times[row][col] = 0
            dived_queue.put([row, col, 0])
        if titup[row][col] == 'S':
            visit_times[row][col] = 0
            visit_queue.put([row, col, 0])
        if titup[row][col] == 'D':
            dest_row = row
            dest_col = col


while not dived_queue.empty():
    row, col, dived_time = dived_queue.get()

    if row > 0 and (titup[row - 1][col] == '.' or titup[row - 1][col] == 'S') and dived_times[row - 1][col] > dived_time + 1:
        dived_times[row - 1][col] = dived_time + 1
        dived_queue.put([row - 1, col, dived_time + 1])
    if col > 0 and (titup[row][col - 1] == '.' or titup[row][col - 1] == 'S') and dived_times[row][col - 1] > dived_time + 1:
        dived_times[row][col - 1] = dived_time + 1
        dived_queue.put([row, col - 1, dived_time + 1])
    if row < r - 1 and (titup[row + 1][col] == '.' or titup[row + 1][col] == 'S') and dived_times[row + 1][col] > dived_time + 1:
        dived_times[row + 1][col] = dived_time + 1
        dived_queue.put([row + 1, col, dived_time + 1])
    if col < c - 1 and (titup[row][col + 1] == '.' or titup[row][col + 1] == 'S') and dived_times[row][col + 1] > dived_time + 1:
        dived_times[row][col + 1] = dived_time + 1
        dived_queue.put([row, col + 1, dived_time + 1])


while not visit_queue.empty():
    row, col, visit_time = visit_queue.get()

    if row > 0 and (titup[row - 1][col] == '.' or titup[row - 1][col] == 'D') and \
            visit_times[row - 1][col] > visit_time + 1 and visit_time + 1 < dived_times[row - 1][col]:
        visit_times[row - 1][col] = visit_time + 1
        visit_queue.put([row - 1, col, visit_time + 1])
    if col > 0 and (titup[row][col - 1] == '.' or titup[row][col - 1] == 'D') and \
            visit_times[row][col - 1] > visit_time + 1 and visit_time + 1 < dived_times[row][col - 1]:
        visit_times[row][col - 1] = visit_time + 1
        visit_queue.put([row, col - 1, visit_time + 1])
    if row < r - 1 and (titup[row + 1][col] == '.' or titup[row + 1][col] == 'D') and \
            visit_times[row + 1][col] > visit_time + 1 and visit_time + 1 < dived_times[row + 1][col]:
        visit_times[row + 1][col] = visit_time + 1
        visit_queue.put([row + 1, col, visit_time + 1])
    if col < c - 1 and (titup[row][col + 1] == '.' or titup[row][col + 1] == 'D') and \
            visit_times[row][col + 1] > visit_time + 1 and visit_time + 1 < dived_times[row][col + 1]:
        visit_times[row][col + 1] = visit_time + 1
        visit_queue.put([row, col + 1, visit_time + 1])

if visit_times[dest_row][dest_col] == 0x7fffffff:
    print('KAKTUS')
else:
    print(visit_times[dest_row][dest_col])

