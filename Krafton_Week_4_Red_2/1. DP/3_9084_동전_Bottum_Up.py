import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    coin_list = list(map(int, sys.stdin.readline().split()))
    target_price = int(sys.stdin.readline())
    case_list = list(0 for _ in range(20002))

    for coin in coin_list:
        case_list[coin] += 1
        for i in range(coin, target_price + 1):
            case_list[i + coin] += case_list[i]
            
    sys.stdout.write(f'{case_list[target_price]}\n')


