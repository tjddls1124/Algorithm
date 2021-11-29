'''
백준 1916번
최소비용 구하기
'''


from heapq import heappush,heappop

from collections import defaultdict
q = []

di = defaultdict(list)
N = int(input())
M = int(input())
import sys 
for i in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    di[a].append((c,b))
st,dest = map(int,input().split())

INF = 10**10
dijk = [INF] * (N+1)
visited = [False] * (N+1)
dijk[st] = 0 

q.append((0,st))

while(len(q)!=0):
    weight, node = heappop(q)
    visited[node] = True
    
    if weight > dijk[node]:
       continue
    
    for v in di[node]:
        if not visited[v[1]]:
            if dijk[v[1]] >  dijk[node] + v[0]:
                dijk[v[1]] = dijk[node] + v[0]
                heappush(q, (dijk[v[1]],v[1] )   )

print(dijk[dest])