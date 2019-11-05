import sys
sys.setrecursionlimit(10000000)


def preprocess(lists: list) -> list:
    lists = sorted(lists)
    for i in range(len(lists) - 1):
        if lists[i][1] > lists[i + 1][1]:
            lists[i + 1][1] = lists[i][1]
    return lists



def main():
    n, w = map(int, input().split())
    V, W = [0] * n, [0] * n
    for i in range(n):
        v_, w_ = map(int, input().split())
        V[i] = v_
        W[i] = w_
    
    n2 = n // 2
    list1 = []
    for i in range(1 << n2):
        sum_v = 0
        sum_w = 0
        for j in range(n2):
            if (i >> j & 1):
                sum_v += V[j]
                sum_w += W[j]
        list1.append([sum_w, sum_v])
    
    list2 = []
    for i in range(1 << (n-n2)):
        i = i << n2
        sum_v = 0
        sum_w = 0
        for j in range(n2, n):
            if (i >> j & 1):
                sum_v += V[j]
                sum_w += W[j]
        list2.append([sum_w, sum_v])

    list1 = preprocess(list1)
    list2 = preprocess(list2)

    # print(list1, list2)
    left = 0
    right = len(list2) - 1
    maximum = 0
    while(left < len(list1)):
        # print(left, right)
        while(True):
            if left == len(list1) - 1:
                break
            if list1[left + 1][0] + list2[right][0] > w:
                break
            left += 1

        while(right >= 0):
            if right == -1:
                break
            if list1[left][0] + list2[right][0] <= w:
                break
            right -= 1
        if left > len(list1) or right < 0:
            break
        maximum = max(maximum, list1[left][1] + list2[right][1])
        right -= 1
    print(maximum)

if __name__ == '__main__':
    main()
