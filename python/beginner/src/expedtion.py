import sys
sys.setrecursionlimit(10000000)
import heapq

def main():
    N, L, P = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    priority_queue = []
    A.append(L)
    B.append(0)

    now_place = 0
    now_gas = P
    num = 0
    for i in range(N + 1):
        if now_gas < 0:
            if len(priority_queue) != 0:
                max_gas = - heapq.heappop(priority_queue)
                now_gas += max_gas
                num += 1
                print(i)
            else:
                print(-1)
                sys.exit()
        else:
            pass
        now_gas -= A[i] - now_place
        now_place = A[i]
        heapq.heappush(priority_queue, - B[i])
    print(num)


if __name__ == '__main__':
    main()
