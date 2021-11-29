'''
백준 11725번
트리의 부모찾기

'''
class Node:
    parent = None
    children = []
    def __init__(self,par=None):
        self.parent = par
    
    def addChild(child):
        self.children.append(Node(child))
        

N = int(input())
import sys
import queue
import collections

q = queue.deque()
dic = collections.defaultdict(list)
res = {}

for i in range(N-1):
    par,child = map(int,sys.stdin.readline().split())
    dic[par].append(child)
    dic[child].append(par)
visited = [False] * (N+1) 

q.append(1)
while len(q)!=0:
    par = q.popleft()
    for v in dic[par]:
        if not visited[v]:
            q.append(v)
            res[v] = par   
            visited[v] = True

for i in range(2,N+1):
    print(res[i])
