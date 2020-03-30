import sys
sys.setrecursionlimit(10000000)
import numpy as np


def depth_search(lakes, i, j):
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y and x == 0:
                continue
            if lakes[i + x][j + y] == 1:
                lakes[i + x][j + y] = 0
                lakes = depth_search(lakes, i + x, j + y)
    return lakes


def main():
    N, W = map(int, input().split())
    lakes = np.zeros((N + 2, W + 2))
    for i in range(N):
        rows = input()
        for j, v in enumerate(rows):
            lakes[i + 1][j + 1] = 0 if v == '.' else 1
    print(lakes)
    
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if lakes[i][j] == 1:
                lakes[i][j] = 0 
                lakes = depth_search(lakes, i, j)
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
