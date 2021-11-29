'''
백준 2206번
벽 부수고 이동하기
'''

import queue
q = queue.deque()

def isAvl(pos,visited):
    x = pos[0]
    y = pos[1]
    if 0<=x<N and 0<=y<M and visited[pos[3]][x][y] == 0:
        if board[x][y]=='0':
            return True
        if pos[3]==0 and board[x][y]=='1':
            pos[3] = 1
            return True
        if board[x][y]=='1':
            return False

    else:
        return False

def bfs():
    q.append([0,0,1,0])
    visited=[]
    
    visited.append([[0]*M for i in range(N)])
    visited.append([[0]*M for i in range(N)])
    
    while(len(q)!=0):
        p = q.popleft()
        x = p[0]
        y = p[1]
        chance = p[3]
        
        if x==N-1 and y==M-1:
            return p[2]
        depth = p[2]+1
        positions = [[x+1,y,depth,chance],[x,y+1,depth,chance],[x-1,y,depth,chance],[x,y-1,depth,chance]]
        for pos in positions:
            if isAvl(pos, visited):
                q.append(pos)
                visited[pos[3]][pos[0]][pos[1]] = 1

    return -1

import sys
N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline()))

# walls = []
# for i in range(N):
#     for j in range(M):
#         if board[i][j]=='1':
#             walls.append((i,j))

# for wall in walls:
#     board[wall[0]][wall[1]] = '0'
#     res = min(res,bfs())
#     board[wall[0]][wall[1]] = '1'

res = bfs()
print(res)

