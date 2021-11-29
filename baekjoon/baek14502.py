'''
백준 14502번
연구소

'''

import sys

def getSafeArea(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                cnt+=1
    return cnt

def bfs(board):
    
    def isAvl(board,p):
        x = p[0]
        y = p[1]
        if 0<=x<N and 0<=y<M and board[x][y]==0 and visited[x][y]==0:
            return True
        else:
            return False
        
        
    visited = [[0]*M for i in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j]==2:
                q.append((i,j))
    
    while(len(q)!=0):
        t = q.popleft()
        x = t[0]
        y = t[1]
        board[x][y] = 2
        
        pos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for p in pos:
            if isAvl(board, p):
                visited[p[0]][p[1]] = 1
                q.append(p)
                


N, M =  map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

se = set()
res = []
spaces = []
block = 3
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            spaces.append((i,j)) 

from itertools import combinations
from copy import deepcopy
from queue import deque

for tuples in list(combinations(spaces, 3)):
    tmp = deepcopy(board)
    for tu in tuples:
        board[tu[0]][tu[1]] = 1
    bfs(board)
    r = getSafeArea(board)
    res.append(r)
    board = tmp
print(max(res))
