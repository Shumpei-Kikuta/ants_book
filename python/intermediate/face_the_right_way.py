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

INF = 10**10

def main():
    N = int(input())
    maps ={'B': 1, "F": 0}
    lists = [maps[c] for c in input()]
    min_num = INF
    min_k = INF
    for k in range(1, N+1):
        dp = [0] * N  # 累積リスト、k番目までで返された回数
        num = 0
        for i in range(N-k+1):
            if i == 0:
                dp[i] = lists[i]
                num += lists[i]
                continue
            if i - k < 0:
                dp[i] = dp[i-1] + (dp[i - 1] + lists[i]) % 2
                num += 1 if (dp[i - 1] + lists[i]) % 2 == 1 else 0
            else:
                dp[i] = dp[i-1] + (dp[i-1] - dp[i - k] + lists[i]) % 2
                num += 1 if (dp[i-1] - dp[i - k] + lists[i]) % 2 == 1 else 0
        flag = True
        for i in range(N-k+1, N):
            if (dp[N-k] - dp[i - k] + lists[i]) % 2 == 0:
                continue
            else:
                flag = False
        if flag and min_num > num:
            min_num = num
            min_k = k


if __name__ == '__main__':
    main()
