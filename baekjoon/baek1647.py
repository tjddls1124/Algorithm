'''
도시분할계획
MST
'''

import sys
from collections import defaultdict
from heapq import *
pq = []
costs = []

N, M = map(int,sys.stdin.readline().split())
dic = defaultdict(list)

visited = [0] * N 

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    dic[a].append((c,b))
    heappush(pq, (c,a,b))

cnt = 1
maps = dict()
for i in range(0,N):
    maps[i] = i

def find(x):
    if maps[x] != x :
        return find(maps[x])
    return x
def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        maps[pb] = pa
    else:
        maps[pa] = pb

def isCycle(a,b):
    fa = find(a)
    fb = find(b)
    if fa==fb:
        return True
    else:
        union(fa,fb)

while pq:
    c,a,b = heappop(pq)
    if isCycle(a-1,b-1): # is cycle
        continue
    costs.append(c)
    if len(costs) == N-1:
        break
print(sum(costs)-max(costs))