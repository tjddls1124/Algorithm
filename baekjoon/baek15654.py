'''
백준 15654번
N과 M 5
'''
import collections
N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)

visited = [0] * len(arr)
def dfs(depth,acc):
    if depth==M:
        for i in acc:
            print(i,end=' ')
        print()
        return    
    for i in range(len(arr)):
        if visited[i] == 1:
            continue
        v = arr[i]
        acc.append(v)
        visited[i] = 1
        dfs(depth+1,acc)
        acc.pop()
        visited[i] = 0
        
dfs(0,collections.deque())