import sys
sys.setrecursionlimit(10000000)
from heapq import heapify, heappop, heappush


def main():
    N = int(input())
    L = [int(c) for c in input().split()]
    heapify(L)
    cost = 0
    for i in range(N - 1):
        x = heappop(L)
        y = heappop(L)
        cost += x + y
        heappush(L, x + y)
    print(cost)


if __name__ == '__main__':
    main()
