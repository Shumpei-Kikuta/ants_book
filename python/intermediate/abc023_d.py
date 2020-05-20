import sys
sys.setrecursionlimit(10000000)
import numpy as np
from heapq import heapify, heappop, heappush
import copy
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
    lists = []
    for i in range(N):
        h, s = map(int, input().split())
        lists.append([h, s])

    left = 0
    right = 10 ** 15
    while(left < right):
        flag = True
        mid = int((left + right) / 2)

        limits = []
        for i in range(N):
            limits.append((mid - lists[i][0]) / lists[i][1])
        limits.sort()

        for i in range(N):
            if limits[i] < i:
                flag = False
                break
        if flag:
            right = mid
        else:
            left = mid + 1
    
    print(left)


if __name__ == '__main__':
    main()
