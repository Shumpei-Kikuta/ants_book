'''
ダイクストラ法
正の重みしか存在しない場合。O(ElogV)
'''

import sys
sys.setrecursionlimit(10000000)
from heapq import heapify, heappop, heappush
import copy

INF = 10 ** 10


def main():
    N = int(input())
    adj_lists = {i: [] for i in range(N)}
    for i in range(N):
        lists = [int(c) for c in input().split()]
        u = lists[0]
        k = lists[1]
        for i in range(k):
            v, c = lists[2 * i + 2], lists[2 * i + 3]
            adj_lists[u].append((v, c))
    
    priority_queue = []
    now = 0
    alreadys = set()
    alreadys.add(now)
    d = [0] + [INF] * (N - 1)
    heappush(priority_queue, (0, 0))
    while(len(priority_queue) != 0):
        _, now = heappop(priority_queue)
        alreadys.add(now)
        edges = adj_lists[now]
        for to_, weight in edges:
            if to_ in alreadys:
                continue
            if d[to_] > d[now] + weight:
                d[to_] = d[now] + weight
                heappush(priority_queue, (d[to_], to_))
    for i, v in enumerate(d):
        print(i, v)

        




if __name__ == '__main__':
    main()
