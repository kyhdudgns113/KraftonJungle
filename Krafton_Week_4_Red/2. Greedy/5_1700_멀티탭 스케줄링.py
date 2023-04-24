import sys

n, k = map(int, sys.stdin.readline().split())

electronics = list(map(int, sys.stdin.readline().split()))

plugs = list(0 for _ in range(n))


#############################################
#
#   각 전자제품인 electronic 에 대해서 돌아간다.
#   - 모든 플러그를 돌면서 어느 플러그에 들어갈 수 있는지를 찾는다.
#   - 플러그에 이미 들어가있으면 돌 필요가 없다.
#   - 플러그가 비어있으면 그곳에 꽂는다.
#   - 플러그가 이미 다 차있으면 플러그에 꽂혀있는 전자제품중 가장 나중에 나오는 전자제품을 뽑는다.
#
#############################################
count = 0
for idx_elec in range(k):

    will_appear = list(101 for _ in range(n))
    is_finished = False

    for idx_plug in range(n):
        if plugs[idx_plug] == electronics[idx_elec]:
            is_finished = True
            break
        if not plugs[idx_plug]:
            plugs[idx_plug] = electronics[idx_elec]
            is_finished = True
            break

        for idx_next_elec in range(idx_elec + 1, k):
            if plugs[idx_plug] == electronics[idx_next_elec]:
                will_appear[idx_plug] = idx_next_elec
                break

    if is_finished:
        continue

    popped_plug = 0
    far_idx = 0
    for idx_will in range(n):
        if far_idx < will_appear[idx_will]:
            far_idx = will_appear[idx_will]
            popped_plug = idx_will

    plugs[popped_plug] = electronics[idx_elec]
    count += 1

print(count)

