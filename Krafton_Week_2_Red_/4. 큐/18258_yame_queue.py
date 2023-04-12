import sys

n = int(sys.stdin.readline())

yame_queue = list(0 for _ in range(2000002))
queue_head = 0
queue_tail = 0  #  queue[tail] 에 값을 넣는다.

for _ in range(n):
    data = sys.stdin.readline().strip()
    if 'push' in data:
        order, num = data.split()
        yame_queue[queue_tail] = int(num)
        queue_tail += 1
    elif 'pop' in data:
        print(-1 if queue_head == queue_tail else yame_queue[queue_head])
        queue_head += 1 if queue_head != queue_tail else 0
    elif 'size' in data:
        print(queue_tail - queue_head)
    elif 'empty' in data:
        print(1 if queue_head == queue_tail else 0)
    elif 'front' in data:
        print(-1 if queue_head == queue_tail else yame_queue[queue_head])
    elif 'back' in data:
        print(-1 if queue_head == queue_tail else yame_queue[queue_tail - 1])

