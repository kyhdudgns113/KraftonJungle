import sys

n = int(sys.stdin.readline())

paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

entire_white = 0
entire_blue = 0


# if, all white, return 1
# elif, all blue, return 10
# else, return 0
def divide_and_merge_paper(max_n, n, left, right, up, down):
    global entire_blue, entire_white, paper

    if n == 1:
        return 10 if paper[up][left] else 1
    else:
        mid_width = (left + right) // 2
        mid_height = (up + down) // 2
        paper_1 = divide_and_merge_paper(n, n // 2, left, mid_width, up, mid_height)
        paper_2 = divide_and_merge_paper(n, n // 2, mid_width + 1, right, up, mid_height)
        paper_3 = divide_and_merge_paper(n, n // 2, left, mid_width, mid_height + 1, down)
        paper_4 = divide_and_merge_paper(n, n // 2, mid_width + 1, right, mid_height + 1, down)

        paper_sum = paper_1 + paper_2 + paper_3 + paper_4

        entire_blue += (paper_sum // 10) % 4
        entire_white += (paper_sum % 10) % 4

        if n == max_n:
            if paper_sum == 4:
                entire_white += 1
            elif paper_sum == 40:
                entire_blue += 1

        match paper_sum:
            case 4:  # case all white
                return 1
            case 40:  # case all blue
                return 10
            case _:  # case mix
                return 0


divide_and_merge_paper(n, n, 0, n - 1, 0, n - 1)

print(entire_white)
print(entire_blue)
