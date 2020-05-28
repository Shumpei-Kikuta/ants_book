import sys
sys.setrecursionlimit(10000000)
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
    while(True):
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            sys.exit()
        num = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                k = bisect_left([s for s in range(1, n + 1)], x - i - j)
                if k + 1<= i or k + 1 <= j or k == n:
                    continue
                num += 1
        print(num)


if __name__ == '__main__':
    main()
