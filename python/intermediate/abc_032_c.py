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
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        s = int(input())
        if s == 0:
            print(N)
            sys.exit()
        S.append(s)
    left = 0
    right = 0
    num = S[0]
    ans = 0
    
    S.append(10**10)
    while(left < N):
        if num <= K:
            # もっと大きくできる
            right += 1
            num *= S[right]
            ans = max(ans, right - left)
        else:
            num /= S[left]
            left += 1
            if left > right:
                right += 1
                num = S[left]
    print(ans)


if __name__ == '__main__':
    main()
