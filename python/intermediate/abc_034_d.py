import sys
sys.setrecursionlimit(10000000)
import numpy as np
from heapq import heapify, heappop, heappush
import copy
# from math import gcd, ceil
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
    N, K = map(int, input().split())
    W = []
    P = []
    for i in range(N):
        w, p = map(int, input().split())
        W.append(w)
        P.append(p)
    
    left = 0
    right = 100
    while(left + 1e-10 < right):
        mid = (left + right) / 2
        lists = []
        for i in range(N):
            element = W[i] * P[i] - mid * W[i]
            lists.append(element)
        lists.sort()
        lists = lists[::-1]

        biggers = lists[:K]
        if np.sum(biggers) >= 0:
            left = mid
        else:
            right = mid
        
    print(left)


if __name__ == '__main__':
    main()
