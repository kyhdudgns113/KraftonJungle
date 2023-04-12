import sys


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class KyhQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            ret_val = self.head.value
            self.head = self.head.next
            self.size -= 1
            return ret_val

    def sizes(self):
        return self.size

    def empty(self):
        return 1 if self.size == 0 else 0

    def front(self):
        return -1 if self.size == 0 else self.head.value

    def back(self):
        return -1 if self.size == 0 else self.tail.value


n = int(sys.stdin.readline())

Q = KyhQueue()

for _ in range(n):
    data = sys.stdin.readline().strip()
    if 'push' in data:
        order, num = data.split()
        Q.push(num)
    elif 'pop' in data:
        print(Q.pop())
    elif 'size' in data:
        print(Q.sizes())
    elif 'empty' in data:
        print(Q.empty())
    elif 'front' in data:
        print(Q.front())
    elif 'back' in data:
        print(Q.back())

