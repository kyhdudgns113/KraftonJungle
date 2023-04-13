import sys


parenthesis = list(sys.stdin.readline().strip())

stack_paren = list(0 for _ in range(len(parenthesis)))
stack_paren_size = 0
stack_num = list(0 for _ in range(len(parenthesis)))
stack_num_size = 0

result_sum = 0

for i in range(len(parenthesis)):
    c = parenthesis[i]
    if c == '(' or c == '[':

        stack_paren[stack_paren_size] = c
        stack_paren_size += 1

        stack_num[stack_num_size] = 1
        stack_num_size += 1
    else:  # 끝맺음이 들어왔을 때
        if stack_paren_size == 0:
            print(0)
            exit()
        if c == ')' and stack_paren[stack_paren_size - 1] != '(' or \
                c == ']' and stack_paren[stack_paren_size - 1] != '[':
            print(0)
            exit()

        if c == ')' and stack_paren[stack_paren_size - 1] == '(':
            stack_num[stack_num_size - 1] *= 2
            if stack_num_size == 1:
                result_sum += stack_num[0]
                # sys.stdout.write(' rf %d' % result_sum)
                stack_num[0] = 0
                stack_paren[0] = 0
                stack_num_size = 0
                stack_paren_size = 0
            elif stack_num_size >= 2 and stack_num[stack_num_size - 2] != 1:
                stack_num[stack_num_size - 2] += stack_num[stack_num_size - 1]
                stack_num[stack_num_size - 1] = 0
                stack_paren[stack_num_size - 1] = 0
                stack_num_size -= 1
                stack_paren_size -= 1
            else:
                stack_num[stack_num_size - 2] = stack_num[stack_num_size - 1]
                stack_num[stack_num_size - 1] = 0
                stack_paren[stack_num_size - 1] = 0
                stack_num_size -= 1
                stack_paren_size -= 1
        elif c == ']' and stack_paren[stack_paren_size - 1] == '[':
            stack_num[stack_num_size - 1] *= 3
            if stack_num_size == 1:
                # sys.stdout.write(' rf %d' % result_sum)
                result_sum += stack_num[0]
                stack_num[0] = 0
                stack_paren[0] = 0
                stack_num_size = 0
                stack_paren_size = 0
            elif stack_num_size >= 2 and stack_num[stack_num_size - 2] != 1:
                stack_num[stack_num_size - 2] += stack_num[stack_num_size - 1]
                stack_num[stack_num_size - 1] = 0
                stack_paren[stack_num_size - 1] = 0
                stack_num_size -= 1
                stack_paren_size -= 1
            else:
                stack_num[stack_num_size - 2] = stack_num[stack_num_size - 1]
                stack_num[stack_num_size - 1] = 0
                stack_paren[stack_num_size - 1] = 0
                stack_num_size -= 1
                stack_paren_size -= 1
    # print(stack_num[0:stack_num_size])


if stack_paren_size != 0:
    print(0)
    exit()

print(result_sum)

