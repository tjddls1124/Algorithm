'''
백준 15652번
N과 M 4

'''


def dfs(li,depth,prev=0):
    if depth==M:
        for i in li:
            print(i,end=' ')
        print()
        return
    for i in range(prev,len(arr)):
        li.append(arr[i])
        dfs(li,depth+1,i)
        li.remove(arr[i])

from itertools import combinations
N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
res = []

dfs([],0)
