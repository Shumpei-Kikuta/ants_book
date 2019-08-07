import numpy as np

def main():
    # N + 1, W + 1の表を書く。
    dp = np.zeros((N + 1, W + 1))
    for i in range(N + 1):
        for j in range(W + 1):
            if i == 0:
                continue
            if w[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j] + v[i])
    print(dp[N][W])
    


if __name__ == '__main__':
    main()
