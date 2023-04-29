import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

result_list = []

is_prime = list(0 for _ in range(2001))
is_sum_prime = list(list(0 for i in range(n)))
prime_list = []

for i in range(2, 2001):
    is_prime[i] = 1
    for prime in prime_list:
        if i % prime == 0:
            is_prime[i] = 0

    if is_prime[i]:
        prime_list.append(i)


#####################################################
#
#   idx_now 번째까지 계산이 완료되었다.
#   나머지 숫자들의 조합으로부터 소수쌍을 만족하는것을 찾는다.
#
#####################################################
def dfs(is_visit):
    global n, is_prime, num_list
    if is_visit == (1 << n) - 1:
        return True

    for idx_start in range(n):
        if not (is_visit & (1 << idx_start)):
            for idx_next in range(n):
                temp_sum = num_list[idx_start] + num_list[idx_next]
                if idx_start != idx_next and not (is_visit & (1 << idx_next)) and is_prime[temp_sum]:
                    ret = dfs(is_visit | (1 << idx_start) | (1 << idx_next))
                    if ret:
                        return True
    return False

is_visit = 1

for i in range(1, n):
    temp_num = num_list[0] + num_list[i]
    if is_prime[temp_num] and dfs(is_visit | 1 << i):
        result_list.append(num_list[i])

result_list.sort()
if result_list:
    print(*result_list)
else:
    print(-1)



