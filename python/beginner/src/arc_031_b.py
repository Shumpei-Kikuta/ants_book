import sys
sys.setrecursionlimit(10000000)
import numpy as np

maps = {'x': -1, 'o': 1}

import copy


A = - np.ones((12, 12))
for i in range(10):
    lines = [maps[i] for i in input()]
    for j, l in enumerate(lines):
        A[i + 1][j + 1] = l

def dfs(i, j, B):
    for s in range(-1, 2):
        for t in range(-1, 2):
            if (s + t) % 2 != 0:
                if B[i + s][j + t] == 1:
                    B[i + s][j + t] = -1
                    dfs(i + s, j + t, B)


def judge(A):
    B = copy.copy(A)
    num = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if B[i][j] == 1:
                num += 1
                if num >= 2:
                    return False
                B[i][j] = -1
                dfs(i, j, B)
    return True


for i in range(1, 11):
    for j in range(1, 11):
        if A[i][j] == 1:
            continue
        A[i][j] = 1
        if judge(A):
            print('YES')
            sys.exit()
        A[i][j] = -1
print('NO')
