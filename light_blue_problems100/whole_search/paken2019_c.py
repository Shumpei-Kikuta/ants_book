import sys
sys.setrecursionlimit(10000000)
import numpy as np
from heapq import heapify, heappop, heappush
import copy
from math import gcd, ceil
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
    N, M = map(int, input().split())
    adj_matrix = np.zeros((N, M))
    for i in range(N):
        lists = [int(c) for c in input().split()]
        for j in range(M):
            adj_matrix[i][j] = lists[j]
    
    max_ = 0
    for j in range(M):
        for k in range(j + 1, M):
            max_sum = 0
            for i in range(N):
                sum_ = max(adj_matrix[i][j], adj_matrix[i][k])
                max_sum += sum_
            max_ = max(max_, max_sum)
    print(int(max_))



if __name__ == '__main__':
    main()
