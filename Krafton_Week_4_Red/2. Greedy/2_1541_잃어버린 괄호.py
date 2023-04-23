import sys

expression = list(sys.stdin.readline().strip())

isMinus = False
temp_num = 0
result = 0
for c in expression:
    if ord('0') <= ord(c) <= ord('9'):
        temp_num *= 10
        temp_num += ord(c) - ord('0')
    else:
        result = result - temp_num if isMinus else result + temp_num
        temp_num = 0
        if c == '-':
            isMinus = True

print(result - temp_num if isMinus else result + temp_num)
