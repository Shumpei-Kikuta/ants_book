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

def flip_around(mass: np.ndarray, s: int, t: int) -> np.ndarray:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i + j) % 2 != 0:
                mass[s+i][t+j] = not mass[s+i][t+j]
    mass[s][t] = not mass[s][t]
    return mass


def main():
    M = int(input())
    N = int(input())
    mass = np.zeros((M + 2, N + 2))
    for i in range(1, M + 1):
        lists = [int(c) for c in input().split()]
        for j in range(1, N + 1):
            mass[i][j] = lists[j-1]
    orig_mass = mass.copy()

    for i in range(1 << N):
        mass = orig_mass.copy()
        matrix = np.zeros((M, N))
        for k in range(N):
            if (i >> k) & 1:
                matrix[0][k] = 1
                mass[1][k+1] = not mass[1][k+1]
                mass[2][k+1] = not mass[2][k+1]  # 自分の下
                mass[1][k] = not mass[1][k]  # 自分の左
                mass[1][k+2] = not mass[1][k+2]  # 自分の右
        for s in range(2, M+1):
            for t in range(1, N+1):
                if mass[s-1][t]:  # 上が黒
                    mass = flip_around(mass, s, t)
                    matrix[s-1][t-1] = 1
            
        flag = True
        for t in range(1, N+1):
            # 一番下が白かどうか
            if mass[M][t]:
                flag = False
                break
        if flag:
            print(matrix)
            sys.exit()
        
    print('IMPOSSIBLE')







if __name__ == '__main__':
    main()
