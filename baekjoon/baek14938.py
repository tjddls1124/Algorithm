'''
백준 14938번
서강그라운드
'''
import sys
N,M,R = map(int,input().split())
items = [0]
items.extend(list(map(int,sys.stdin.readline().split())))

INF = 10 ** 6
maps = [[INF] * (N+1) for _ in range(N+1)]
dp = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(R):
    st,dest,weight = map(int,sys.stdin.readline().split())
    maps[st][dest] = weight
    maps[dest][st] = weight

for i in range(N+1):
    maps[i][i] = 0 

## floyd
from collections import deque


for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

maxItems = 0
for i in range(N+1):
    res = 0
    for j in range(N+1):
        if maps[i][j] <= M:
            res += items[j]
    maxItems = max(maxItems,res)
print(maxItems)