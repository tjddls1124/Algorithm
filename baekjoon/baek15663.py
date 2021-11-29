'''
백준 15663번
N과 M
'''

N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr = sorted(arr)
se = set()
import copy
visited = [False] * len(arr)
def dfs(depth, res):
    if depth == M :
        se.add(tuple(res))
        return
    for t in range(len(arr)):
        if visited[t]:
            continue
        visited[t] = True
        res.append(arr[t])
        dfs(depth+1,res)
        res.pop()
        visited[t] = False
        
dfs(0,[])

for li in sorted(list(se)):
    for v in li:
        print(v,end=' ')
    print()