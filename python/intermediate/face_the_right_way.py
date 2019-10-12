# 頭がこんがらがる。
# 境界条件が曖昧な時はwhileで問いた方が良い

INF = 10000


def solve(A: list, k: int):
    """
    k頭連続反転するとき、必要な最小操作回数。
    達成できないならば、INFを返す
    """
    N = len(A)
    G = [0] * N
    sum_ = 0  # i番目を反転させた回数
    rev_num = 0

    for i in range(0, N - k + 1):
        if i - k >= 0:
            sum_ = (sum_ + G[i - k]) % 2

        if (A[i] + sum_) % 2 == 0:
            G[i] = 0
        else:
            rev_num += 1
            G[i] = 1
        sum_ = (sum_ + G[i]) % 2

    for i in range(N - k + 1, N):
        sum_ = (sum_ + G[i - k]) % 2
        if (A[i] + sum_) % 2 == 0:
            pass
        else:
            return INF
    return rev_num


def main():
    N = int(input())
    string = input()

    # Aの初期化
    A = []
    for i in string:
        if i == "B":
            A.append(1)  # 後ろ向きなら1
        else:
            A.append(0)  # 前向きなら0

    M = sum(A)
    min_k = 1
    for k in range(2, N+1):
        m = solve(A, k)
        if m < M:
            min_k = k
            M = m

    print(M, min_k)


if __name__ == '__main__':
    main()
