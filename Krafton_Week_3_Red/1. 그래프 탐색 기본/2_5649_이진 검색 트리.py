import sys
from queue import Queue

sys.setrecursionlimit(10**7)

input_q = Queue()

while True:
    try:
        input_q.put(int(sys.stdin.readline()))
    except:
        break

vlr = list(input_q.queue)
n = len(vlr)


def vlr_to_lrv(start, end):
    global vlr
    v = start
    left = start + 1
    right = left

    if start > end:
        return

    while right <= end and vlr[v] >= vlr[right]:
        right += 1

    vlr_to_lrv(left, right - 1)
    vlr_to_lrv(right, end)
    sys.stdout.write(f'{vlr[v]}\n')


vlr_to_lrv(0, n - 1)
