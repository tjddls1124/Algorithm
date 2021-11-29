'''
문제집
'''
from collections import defaultdict
from queue import PriorityQueue

from heapq import *
import sys
N, M = map(int,input().split())

dic = defaultdict(list)
arr = [0] * (N+1)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    dic[a].append(b)
    arr[b]+=1

pq = []
        
while True:
    for i in range(1,N+1):
        if arr[i]==0:
            heappush(pq,i)
            arr[i]-=1
    if len(pq)==0:
        break
    val = heappop(pq)
    print(val, end=' ')
    for v in dic[val]:
        arr[v]-=1