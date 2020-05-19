import sys
sys.setrecursionlimit(10000000)
import numpy as np
from heapq import heapify, heappop, heappush
import copy
from collections import deque
# queueとして使う場合 push, popleftを使う
from bisect import bisect_left, bisect_right


def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    B = [int(c) for c in input().split()]
    C = [int(c) for c in input().split()]

    A.sort()
    B.sort()
    C.sort()

    num = 0
    for j in range(N):
        bj = B[j]
        c = bisect_right(C, bj)
        a = bisect_left(A, bj)
        num += a * (N - c)
    
    print(num)


if __name__ == '__main__':
    main()
