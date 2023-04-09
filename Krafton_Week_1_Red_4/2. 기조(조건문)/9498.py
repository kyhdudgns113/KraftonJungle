import sys, math

a = int(sys.stdin.readline())

match a//10:
    case 10: print("A")
    case 9: print("A")
    case 8: print("B")
    case 7: print("C")
    case 6: print("D")
    case _: print("F")

