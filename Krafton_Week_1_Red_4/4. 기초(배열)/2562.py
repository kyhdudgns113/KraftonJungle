import sys

list_number = [int(sys.stdin.readline()) for _ in range(9)]

print(max(list_number))
print(list_number.index(max(list_number)) + 1)
