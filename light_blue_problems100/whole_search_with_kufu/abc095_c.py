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
    A, B, C, X, Y = map(int,input().split())
    max_C_num = 2 * max(X, Y)
    left_x = X
    left_y = Y
    min_price = 10 ** 10
    for c in range(0, max_C_num + 1, 2):
        left_x = X - c // 2
        left_y = Y - c // 2
        price = C * c
        if price > min_price:
            continue
        if left_x > 0:
            price += A * left_x
        if left_y > 0:
            price += B * left_y
        min_price = min(price, min_price)
    print(min_price)


if __name__ == '__main__':
    main()
