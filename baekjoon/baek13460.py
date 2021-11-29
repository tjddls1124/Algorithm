'''
구슬 탈출2
'''

import sys
N,M = map(int,input().split())

board = []
x_r,y_r,x_b,y_b = 0,0,0,0
for i in range(N):
    board.append(list(sys.stdin.readline()))
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            x_r,y_r = i,j
        if board[i][j] == 'B':
            x_b,y_b = i,j

visited = set()

def isAvl(x,y):
    return 0<=x<N and 0<=y<M and board[x][y]!='#' 

import queue

def getPos(x,y,depth,color):
    n_delta = [(0,1),(0,-1),(1,0),(-1,0)]
    arr = []
    for delta in n_delta:
        isBall = False
        nx = x
        ny = y
        while True:
            nx = nx+delta[0]
            ny= ny+delta[1]
            if board[nx][ny] == 'O':
                arr.append("goal")
                break 
            if board[nx][ny] == '#':
                if isBall:
                    arr.append((nx-delta[0]*2,ny-delta[1]*2))
                else:
                    arr.append((nx-delta[0],ny-delta[1]))
                break
            if board[nx][ny] == 'R' or board[nx][ny]=='B':
                isBall=True
    return arr

visited.add((x_r,y_r,x_b,y_b))
q = queue.deque()
q.append((x_r,y_r,x_b,y_b,0))
    
def bfs():
    while len(q)!=0 :
        po = q.popleft()
        x_r = po[0]
        y_r = po[1]
        x_b = po[2]
        y_b = po[3]
        
        board[x_r][y_r] = 'R'
        board[x_b][y_b] = 'B'

        depth = po[4]
        
        if depth>9:
          print("-1")
          quit()

        r_positions = getPos(x_r, y_r, depth,'r')
        b_positions = getPos(x_b, y_b, depth,'b')
        
        
        board[x_r][y_r] = '.'
        board[x_b][y_b] = '.'
        for i in range(4):
            r = r_positions[i]
            b = b_positions[i]
            if r=='goal' and b!='goal':
                print(depth+1)
                quit()
            if b=='goal':
                continue
            
            if not (r[0],r[1],b[0],b[1]) in visited:
                visited.add((r[0],r[1],b[0],b[1]))
                q.append((r[0],r[1],b[0],b[1],depth+1))
                
bfs()
print("-1")