import sys
sys.setrecursionlimit(10000000)


def main():
    n = int(input())
    k = int(input())
    W = []
    V = []
    for i in range(n):
        w, v = map(int, input())
        W.append(w)
        V.append(v)
    num = 0
    left = 0
    right = 10 ** 12
    while(num < 100):
        mid = (left + right) // 2
        lists = []
        for i in range(n):
            lists.append(v[i] - mid * w[i])
        lists.sort(reverse=True)
        if sum(lists[:k]) >= 0:
            # 平均はもっと大きくできる
            left = mid
        else:
            right = mid - 1


if __name__ == '__main__':
    main()
