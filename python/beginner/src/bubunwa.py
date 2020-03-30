import sys
sys.setrecursionlimit(10000000)


def rec(A, n, k, sum_, cnt):
    if sum_ == k:
        return True
    elif cnt < n:
        return rec(A, n, k, sum_ + A[cnt], cnt + 1) | rec(A, n, k, sum_, cnt + 1)
    else:
        return False


def main():
    n = int(input())
    A = [int(a) for a in input().split()]
    k = int(input())

    if rec(A, n, k, 0, 0):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
