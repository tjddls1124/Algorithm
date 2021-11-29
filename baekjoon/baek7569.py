'''
백준 7569번
토마토 (3차원)
'''

## 모두 익어있다면 return 0 
## 0이 남는다면 -1

from collections import deque
import sys

maps = []
tomatos = []

M,N,H = map(int,input().split())
allMature = True

for i in range(H):
    arr = []
    for j in range(N):
        li = list(map( int, sys.stdin.readline().split() ))
        arr.append(li)
        for index, k in enumerate(li):
            if k==1:
                tomatos.append((i,j,index))
            if k==0:
                allMature = False
    maps.append(arr)

q = deque()
visited = []
for _ in range(H):
    visited.append([[False]*M for _ in range(N)])

def bfs():
    maxDay = 0
    while q:
        i,j,k,day= q.popleft()
        if maps[i][j][k] == 0:
            maps[i][j][k] = 1
        if maps[i][j][k]==-1:
            continue
        maxDay = max(maxDay,day)
        points = [(i-1,j,k),(i+1,j,k),(i,j-1,k),(i,j+1,k),(i,j,k+1),(i,j,k-1)]
        
        for po in points:
            x = po[0]
            y = po[1]
            z = po[2]
            if 0 <=x<H and 0<=y<N and 0<=z<M and not visited[x][y][z]:
                visited[x][y][z] = True
                q.append((x,y,z,day+1))
    for arr in maps:
        for li in arr:
            if 0 in li:
                print("-1")
                return 
    print(maxDay)

for tomato in tomatos:
    visited[tomato[0]][tomato[1]][tomato[2]] = True
    q.append((*tomato,0))

if allMature:
    print("0")
else:
    bfs()