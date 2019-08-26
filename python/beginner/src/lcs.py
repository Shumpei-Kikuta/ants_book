import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def exec_lcs(s: str, t: str, n: int, m: int) -> int:
    TAB = []
    for i in range(n + 1):
        line = []
        for j in range(m + 1):
            line.append(0)
        TAB.append(line)
    # print(TAB)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                TAB[i][j] = TAB[i-1][j-1] + 1
            else:
                TAB[i][j] = max(TAB[i-1][j], TAB[i][j-1])
    return TAB[n][m]


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    assert(len(s) == n)
    assert(len(t) == m)

    print(exec_lcs(s, t, n, m))

if __name__ == '__main__':
    main()