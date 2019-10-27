import sys
sys.setrecursionlimit(10000000)


INF = 100000000

V, E = map(int, input().split())
adjacency_matrix = []
for i in range(V):
    adjacency_matrix.append([-1] * V)
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
    V = len(adjacency_matrix)
    if dp[S][v] >= 0:
        # already visited
        return dp[S][v]
    if S == (V << 1) - 1 and v == 0:
        # already visited the all places and now place is the goal
        dp[S][v] = 0
        return dp[S][v]
    res = INF
    for u in range(V):
        if not ((S >> u) & 1):
            # never been to u
            res = min(res, solve(S | (1 << u), u))
    dp[S][v] = res
    return res


def main():        
    print(solve(0, 0))
    

if __name__ == '__main__':
    main()
