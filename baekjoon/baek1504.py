'''
백준 1504번
특정한 최단경로

3번 다익스트라 반복해서 해결
'''

import sys

N, E = map(int, sys.stdin.readline().split())
INF = 10**10

board = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(E):
    st,end, weight = map(int, sys.stdin.readline().split())
    board[st][end] = min(board[st][end], weight)
    board[end][st] = min(board[end][st], weight)
    
v1,v2 = map(int,sys.stdin.readline().split())


fl = [[list()] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    board[i][i] = 0


##djkstra
from heapq import *
def dijk(start):
    visited =[0] * (N+1)
    shortest = [INF] * (N+1)
    shortest[start] = 0
    q = []
    heappush(q, (0,start)) # weight,end
    while q:
        weight,end = heappop(q)
        if visited[end] == 1:
            continue
        visited[end] = 1
        
        for i in range(1,N+1):
            new_w = weight + board[end][i]
            if shortest[i] > new_w:
                heappush(q, (new_w,i))
                shortest[i] = new_w
                if len(fl[start][i])==0:
                    fl[start][i] = set()
                    fl[start][i].add(end)
    return shortest
arr = [0] * (N+1)
arr[1] = dijk(1)
arr[v1] = dijk(v1)
arr[v2] = dijk(v2)
res = 0
if v1 in fl[1][N] and v2 in fl[1][N]:
    res = (arr[1][N])
elif v2 in fl[1][v1]:
    res = arr[1][v1] + arr[v1][N]
elif v1 in fl[1][v2]:
    res = arr[1][v2] + arr[v2][N]
else:
    res = min(arr[1][v1] + arr[v1][v2] + arr[v2][N] , arr[1][v2] + arr[v2][v1] + arr[v1][N] )

if res >= INF:
    print("-1")
else:
    print(res) 