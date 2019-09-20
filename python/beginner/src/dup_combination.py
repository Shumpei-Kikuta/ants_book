import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    n = int(input())
    m = int(input())
    a = [int(c) for c in input().split()]
    M = int(input())

    dp = []
    for i in range(n + 1):
        inline = []
        for j in range(m + 1):
            inline.append(0)
        dp.append(inline)

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] > j - 1: # i番目の数がjより小さい時
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1 - a[i - 1]]
    print(dp[n][m] % M)


if __name__ == '__main__':
    main()