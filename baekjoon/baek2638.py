'''
치즈
bfs
'''

from collections import deque

AIR = 2
INC = 3

N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        pos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for p in pos:
            i = p[0]
            j = p[1]
            if 0 <= i < N and 0<= j < M and arr[i][j] == 0:
                arr[i][j] = AIR
                q.append((i,j))
def isC(i,j):
    cnt = 0
    pos = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    for p in pos:
        x = p[0]
        y = p[1]
        if 0 <= x < N and 0<= y < M:
            if arr[x][y]==AIR:
                cnt+=1
    if cnt>=2:
        return True
    else:
        return False
from copy import deepcopy
ans = 0 
while True:
    
    allDisappear = True
    bfs()
    new_arr = deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == AIR:
                new_arr[i][j] = 0 
            if arr[i][j] == 1:
                allDisappear = False
                if isC(i,j) :
                    new_arr[i][j] = 0
    if allDisappear:
        break
    arr = new_arr
    ans +=1
print(ans)