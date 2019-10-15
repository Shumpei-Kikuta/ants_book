def factorial_devided_n(x: int, n: int, mod: int):
    res = 1
    while n > 0:
        if (n & 1):  # if n has 1 at the least digit
            res = (res * x) % mod
        x = x * x
        n >>= 1
    return res


def carmichael(n: int):
    for x in range(2, n):
        nx = factorial_devided_n(x, n, n)
        if nx % n == x:
            continue
        else:
            return False
    return True


def main():
    n = int(input())
    if carmichael(n):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
