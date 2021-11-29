'''
백준 1697번
숨바꼭질

BFS
'''
N, K = map(int, input().split())
from collections import deque 
#bfs
q= deque()

visited = [0] * (3*max(N,K)+5)


q.append((N,0))
while True:
    p = q.popleft()
    x = p[0]
    depth = p[1]
    if x == K:
        print(depth)
        break
    positions = [(x+1,depth+1),(x-1,depth+1),(2*x,depth+1)]
    for pos in positions:
        if not 0<= pos[0]< 3*max(N,K) :
            continue
        if visited[pos[0]] != 0:    
            continue
        visited[pos[0]] = 1
        q.append(pos)


     

    
