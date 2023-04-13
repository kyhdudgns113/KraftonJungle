import sys

n = int(sys.stdin.readline())

circles = list([0, 0] for _ in range(n))

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles[_] = [x, r]

areas = list([0, 0] for _ in range(n))

for i, circle in enumerate(circles):
    areas[i] = [circle[0] - circle[1], circle[0] + circle[1]]

areas.sort(key=lambda x: (x[0], -x[1]))
# print(areas)


right = 2000000001
left = -2000000001
previous_left = right
count_areas = n + 1
stack = list([0, 0] for _ in range(n))
stack_size = 0

for i in range(n):
    area = areas[i]
    # sys.stdout.write(f'({area[0]}, {area[1]}) lr({left}, {right}) ')
    if stack_size == 0:  # 스택이 비어있을 때
        # sys.stdout.write(f' e ')
        stack[stack_size] = area
        left = area[0]
        right = area[1]
        stack_size += 1
    else:
        if left <= area[0] and area[1] <= right:  # 스택의 최상단 안에 포함이 될 때
            # sys.stdout.write(f' i ')
            left = area[0]
            right = area[1]
            stack[stack_size] = area
            stack_size += 1
        else:
            #  area 의 왼쪽에 있는 스택을 제거한다.
            #  탈출조건이 있다.
            while True:
                if stack_size == 0:
                    break
                #  area 의 왼쪽이 스택의 최상단의 오른쪽과 맞닿아 있으면서
                #  맞닿아 있는 스택이 하나밖에 없을 때
                if stack[stack_size - 1][1] >= area[0] and \
                        not (stack_size >= 2 and stack[stack_size - 2][1] == area[0]):
                    break
                #  스택의 최상단 안에 포함이 될 때, 스택 인덱스가 변하기때문에 넣어줘야됨
                if left <= area[0] and area[1] <= right:
                    break
                # sys.stdout.write('w')
                # sys.stdout.write(f'({left} {right}) ')
                stack[stack_size - 1] = [0, 0]
                stack_size -= 1

                left = stack[stack_size - 1][0]
                right = stack[stack_size - 1][1]
            if stack_size >= 2 and right == area[0] and area[1] == stack[stack_size - 2][1]:
                #  area 가 들어감으로써 공간이 나뉘어질때
                if stack[stack_size - 2][0] == stack[stack_size - 1][0]:
                    # sys.stdout.write(' 1 ')
                    right = area[1]
                    left = area[0]
                    count_areas += 1
                    stack[stack_size - 1] = area
                #  area 가 들어감으로써 스택의 최상단과 만나기는 하지만, 공간이 나뉘어지지는 않을 때
                else:
                    # sys.stdout.write(' 2 ')
                    right = area[1]
                    left = area[0]
                    stack[stack_size - 1] = area
            #  이 역시 area 가 들어감으로써 스택의 최상단과 만나기는 하지만, 공간이 나뉘어지지는 않을 때
            elif right == area[0]:
                # sys.stdout.write(' 3and4 ')
                stack[stack_size - 1][1] = area[1]
                stack[stack_size] = area
                stack_size += 1
                left = stack[stack_size - 1][0]
                right = area[1]
            #  나머지 모든 경우
            else:
                # sys.stdout.write(' 5to8 ')
                stack[stack_size] = area
                stack_size += 1
                left = area[0]
                right = area[1]

    # print(stack)


print(count_areas)



