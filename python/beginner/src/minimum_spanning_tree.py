import sys
sys.setrecursionlimit(10000000)
from heapq import heapify, heappop, heappush
import copy


def main():
    V, E = map(int, input().split())
    adj_lists = {i: [] for i in range(V)}
    for i in range(E):
        s, t, w = map(int, input().split())
        adj_lists[s].append((t, w))
        adj_lists[t].append((s, w))
    
    priority_queue = []
    now = 0
    alreadys = set()
    alreadys.add(now)

    nexts = adj_lists[now]
    for next_, w in nexts:
        if next_ in alreadys:
            continue
        heappush(priority_queue, (w, next_))

    weight = 0
    num = 0
    while(len(alreadys) != V):
        w, now = heappop(priority_queue)
        if now in alreadys:
            continue
        weight += w
        alreadys.add(now)
        nexts = adj_lists[now]
        for next_, w in nexts:
            if next_ in alreadys:
                continue
            heappush(priority_queue, (w, next_))

    print(weight)


if __name__ == '__main__':
    main()
