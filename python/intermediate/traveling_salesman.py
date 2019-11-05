import sys
sys.setrecursionlimit(10000000)


INF = 100000000

V, E = map(int, input().split())
adjacency_matrix = []
for i in range(V):
    adjacency_matrix.append([INF] * V)
for i in range(E):
    from_, to_, d = map(int, input().split())
    adjacency_matrix[from_][to_] = d
dp = []
for i in range(1 << V):
    dp.append([-1] * V)


def solve(S, v):
    """
    S: set for the nodes already visited
    v: current node
    """
    if dp[S][v] >= 0:
        # already visited
        return dp[S][v]
    elif S == (1 << V) - 1 and v == 0:
        # already visited the all places and now place is the goal
        dp[S][v] = 0
        return dp[S][v]
    else:
        res = INF
        for u in range(V):
            if not ((S >> u) & 1):
                # never been to u
                res = min(res, solve(S | (1 << u), u) + adjacency_matrix[v][u])
        dp[S][v] = res
        return dp[S][v]


def main():
    if solve(0, 0) >= INF:
        print(-1)
    else:
        print(solve(0, 0))
    # print(dp)
    

if __name__ == '__main__':
    main()
