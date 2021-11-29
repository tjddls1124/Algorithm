'''
백준1005번
ACM Craft
'''
import sys
sys.setrecursionlimit(10**8)

INF = 10**12
arr = []
def dfs(target):
    if len(dic[target])==0:
        visited[target]=bt[target]
        return bt[target]
    minBt = 0 
    for x in dic[target]:
        val = 0
        if visited[target]==-1:
            val = dfs(x)
        else:
            val = visited[x]
        minBt = max(minBt, val)
    visited[target] = minBt+bt[target]
    return minBt+bt[target] 

T = int(input())
from collections import defaultdict

for t in range(T):
    N, K = map(int,input().split())
    bt = list(map(int,input().split())) #build time
    visited = [-1] * (N+1) 
    dic = defaultdict(list)
    for k in range(K):
        x,y = map(int,sys.stdin.readline().split())
        dic[y-1].append(x-1)

    target = int(input())-1
    dfs(target)
    print(visited[target])
