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
    N = int(input())
    S = input()
    most_left = {i: -1 for i in range(10)}
    for i in range(len(S)):
        s = int(S[i])
        if most_left[s] == -1:
            most_left[s] = i
    
    wholes = [False] * 1000
    sum_ = 0
    
    for i, first_idx in most_left.items():
        if first_idx == -1:
            continue
        alreadys = [False] * 10
        for second_idx in range(first_idx + 1, N):
            if alreadys[int(S[second_idx])]:
                continue
            alreadys[int(S[second_idx])] = True
            for third_idx in range(second_idx + 1, N):
                number = int(S[first_idx] + S[second_idx] + S[third_idx])
                if wholes[number] is False:
                    wholes[number] = True
                    sum_ += 1
    print(sum_)



        




if __name__ == '__main__':
    main()
