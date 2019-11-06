import sys
sys.setrecursionlimit(10000000)

INF = 1000

n = int(input())
m = int(input())
a = int(input())
b = int(input())
T = [int(c) for c in input().split()]

dp = []
for i in range(1 << n):
    inner = []
    for j in range(m):
        inner.append(INF)
    dp.append(inner)

adj = []


def solve(S, now):
    while(True):
        if now == b:
            # 探索終えた
            dp[S][now] = 0
            return dp[S][now]
        elif S == (1 << n - 1):
            # ゴールにたどり着けない
            dp[S][now] = INF
            return dp[S][now]
        else:
            res = INF
            for next_ in range(m):
                for i in range(n):
                    if S >> i & 1:
                        # すでにi番目のチケットを使った
                        continue
                    else:
                        res = min(res, solve(S | i, next_) + adj[now][next_])

            dp[S][now] = res
            return res
    

def main():    
    S = 0
    now = a
    solve(S, now)


if __name__ == '__main__':
    main()
