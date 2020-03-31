import sys
sys.setrecursionlimit(10000000)
from collections import deque
import numpy as np


INF = 10 ** 10


def main():
    N, M = map(int, input().split())
    meiros = np.ones((N + 2, M + 2)) * (-1)
    d = np.ones((N + 2, M + 2)) * INF
    for i in range(N):
        input_ = input()
        for j, v in enumerate(input_):
            if v == '.':
                meiros[i + 1][j + 1] = INF
            elif v == '#':
                meiros[i + 1][j + 1] = -1
            elif v == 'S':
                meiros[i + 1][j + 1] = 0
                S = (i + 1, j + 1)
            else:
                G = (i + 1, j + 1)
                meiros[i + 1][j + 1] = INF

    queue = deque()
    queue.append(S)

    while(len(queue) != 0):
        now = queue.popleft()
        if now == G:
            print(meiros[now[0]][now[1]])
            break
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i + j) % 2 == 0:
                    continue
                if meiros[now[0] + i][now[1] + j] == INF:
                    queue.append((now[0] + i, now[1] + j))
                    meiros[now[0] + i][now[1] + j] = meiros[now[0]][now[1]] + 1


if __name__ == '__main__':
    main()
