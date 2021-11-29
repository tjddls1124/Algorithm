'''
백준 15656번
N과 M

dfs
'''
import sys
from collections import deque

N, M = map(int,input().split())
arr = list(map(int, (sys.stdin.readline().split())))

arr = sorted(arr)

def dfs(st,depth,res):
    if depth==M:
        for r in res:
            print(r,end=' ')
        print()
        return
    for i in range(st,len(arr)):
        res.append(arr[i])
        dfs(i,depth+1,res)
        res.pop()

res = deque()

dfs(0,0,res)
    