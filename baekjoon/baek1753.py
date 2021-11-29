'''
백준 1753번
최단경로

다익스트라, 프림 알고리즘
'''


'''
다익스트라 사용시 pq에서 꺼낸 뒤에 visit 체크(넣을때 하면 안됨)

튜플 등은 앞에서부터 (a,b,c) a->b->c 순으로 사전순 정렬됨 (heapq 사용시 유의)

'''
import sys
import heapq
from collections import defaultdict
pq = heapq
heap=[]

INF = 10**6

V, E = map(int, input().split())
st = int(input())
w = [ defaultdict(lambda: INF) for i in range(V+1) ]
for i in range(E):
    fr, to , weight = map(int,sys.stdin.readline().split())
    w[fr][to] = min(w[fr][to],weight)

dijk = [INF] * (V+1)
dijk[st] = 0
visited = [0] * (V+1)
pq.heappush(heap, (0,st))
visited[st] = 1
while(len(heap)!=0):
    wei, n= pq.heappop(heap)
    visited[n] = 1
    
    if wei > dijk[n]: #현재값보다 간선값이 크다면 제외
        continue
    
    for i,weight in w[n].items():
        if weight>=INF:
            continue
        if dijk[i] > dijk[n]+weight: # 길이가 더 짧아 갱신되는 경우만 pq에 푸시
            dijk[i] = dijk[n]+weight
            if visited[i] == 0:
                pq.heappush(heap,(dijk[i],i)) 
        

for i in range(1,len(dijk)):
    if dijk[i] >= INF:
        print("INF")
    else:
        print(dijk[i])