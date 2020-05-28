import sys
sys.setrecursionlimit(10000000)
import numpy as np
from heapq import heapify, heappop, heappush
import copy
from math import ceil
from collections import deque
# queueとして使う場合 push, popleftを使う
from bisect import bisect_left, bisect_right
# bisect_left: 配列の順序関係が崩れない条件で挿入することができる一番左の点
# bisect_right: 配列の順序関係が崩れない条件で挿入することができる一番右の点
# A = [1, 1, 1, 2, 2, 2, 4]
# print(bisect_left(A, 2))  # 3
# print(bisect_right(A, 2))  # 6
# print(bisect_left(A, 3))  # 6
# print(bisect_right(A, 3))  # 6


def main():
    N = int(input())
    num = 0
    for i in range(9, N + 1):
        if i % 2 == 0:
            continue
        d = 0
        for j in range(1, N + 1):
            if i % j == 0:
                d += 1 
        if d == 8:
            num += 1
    print(num)

if __name__ == '__main__':
    main()
