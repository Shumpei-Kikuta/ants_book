import sys
sys.setrecursionlimit(10000000)


import sys
sys.setrecursionlimit(10000000)


# 1. 再帰関数
# def main():
#     n = int(input())
#     a = [int(c) for c in input().split()]
#     k = int(input())
#     def rec(sum_, idx):
#         if idx == n:
#             if sum_ == k:
#                 return True
#             else:
#                 return False
#         else:
#             return rec(sum_+a[idx], idx+1) | rec(sum_, idx+1)

#     if rec(0, 0):
#         print('Yes')
#     else:
#         print('No')

# 1. 再帰関数
def main():
    n = int(input())
    a = [int(c) for c in input().split()]
    k = int(input())
    for i in range(1 << n):
        sum_ = 0
        for j in range(n):
            if (i >> j) & 1:
                sum_ += a[j]
        if sum_ == k:
            print('Yes')
            sys.exit()
    else:
        print('No')



if __name__ == '__main__':
    main()

