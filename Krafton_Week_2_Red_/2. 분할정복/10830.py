import sys, copy


n, b = map(int, sys.stdin.readline().split())

a = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

a2k = []


def get_element_matrix(n):
    matrix = list(list(0 for _ in range(n)) for __ in range(n))
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def mat_mul(ma, mb, n):
    matrix = list(list(0 for _ in range(n)) for __ in range(n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] = (matrix[i][j] + ma[i][k] * mb[k][j]) % 1000
    return matrix


def get_apowb():
    global n, a2k, b

    # set a0
    for i in range(n):
        for j in range(n):
            a[i][j] = a[i][j] % 1000

    temp_matrix = copy.deepcopy(a)
    for i in range(40):
        a2k.append(temp_matrix)
        temp_matrix = mat_mul(temp_matrix, temp_matrix, n)

    temp_matrix = get_element_matrix(n)
    idx = 0
    while b:
        if b & 1:
            temp_matrix = mat_mul(temp_matrix, a2k[idx], n)
        idx += 1
        b //= 2

    return temp_matrix


apowb = get_apowb()

for row in apowb:
    for col in row:
        sys.stdout.write(str(col) + ' ')
    sys.stdout.write('\n')




