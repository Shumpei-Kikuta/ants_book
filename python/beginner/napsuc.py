def main():
    # 入力の処理
    N, W = map(int, input().split())
    w = [0]
    v = [0]
    for i in range(N):
      v_i, w_i = map(int, input().split())
      v.append(v_i)
      w.append(w_i)

    # dpの表のinitialize
    dp = []
    for i in range(N + 1):
        inner = []
        for j in range(W + 1):
            inner.append(0)
        dp.append(inner)

    # 漸化式
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if w[i] > j:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i], dp[i][j - 1])
    print(int(dp[N][W]))


if __name__ == '__main__':
    main()
