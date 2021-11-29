'''
백준 1238번

파티

dijkstra

'''
from collections import defaultdict
from heapq import *

dic = defaultdict(list)
dic_inv = defaultdict(list)
N,M,X = map(int,input().split())
for _ in range(M):
    fr,to,we = map(int,input().split())
    dic[fr].append((we,to))
    dic_inv[to].append((we,fr))

def dijk(dic):
    ##dijkstra
    INF = 10**8
    hq = []
    paths = [INF] * (N+1)
    paths[X] = 0
    visited = [0] * (N+1)
    for item in dic[X]:
        heappush(hq, item)
    while len(hq)!=0:
        w,to = heappop(hq)
        if visited[to] == 1:
            continue    
        visited[to] = 1
        if w <= paths[to]:
            paths[to] = w
        else:
            continue
        for item in dic[to]:
            new_w = item[0] + w
            if new_w< paths[item[1]]:
                paths[item[1]] = new_w
                heappush(hq, (new_w,item[1]))
    return paths
re_dic = dijk(dic)
re_dic_inv = dijk(dic_inv)

result = [sum(x) for x in zip(re_dic,re_dic_inv)]
del result[0]
print(max(result))
