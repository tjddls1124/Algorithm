'''
백준 1197번
최소 스패닝 트리

'''

V,E = map(int, input().split())
import sys
from queue import PriorityQueue
from collections import defaultdict
q = PriorityQueue()

minE = 10**8
minVec = None
dic = defaultdict(list)

for i in range(E):
    a,b,w = map(int,sys.stdin.readline().split())
    dic[a].append((b,w))
    dic[b].append((a,w))
    if w < minE:
        minVec = (w,a,b)
        minE = w

forest = set()
res = 0

q.put(minVec)

while(not q.empty()):
    tup = q.get()
    
    if tup[1] in forest and tup[2] in forest: #is cycle
        continue

    res+=tup[0]

    if not tup[2] in forest:    
        for newNode,weight in dic[tup[2]]:
            q.put((weight,tup[2],newNode))
        forest.add(tup[2])
        
    if not tup[1] in forest:    
        for newNode,weight in dic[tup[1]]:
            q.put((weight,tup[1],newNode))
        forest.add(tup[1])
    
print(res)