from collections import deque
def isAval(x,y):
    if 0 <= x < N and 0 <= y < M and board[x][y]=='1':
        return True
    return False

def bfs(pos):
    q = deque()
    q.append([0,0,1])
    
    while(len(q)!=0):
        po = q.popleft()
        
        x = po[0]
        y = po[1]
        depth = po[2]
        
        if not isAval(x, y):
            continue
        
        if x==N-1 and y == M-1:
            ans.append(depth)    
            break
        
        if visited[x][y] != 0:
            continue
            
        visited[x][y] = depth
        position = [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]    
        for p in position:
            p.append(depth+1)
            q.append(p)
    
    

def dfs(pos, depth):
    x = pos[0]
    y = pos[1]
    
    
    
        
N , M = map(int, input().split())
ans = []
board = []
for i in range(N):
    board.append(input())

visited = [[0]*M for i in range(N)]

bfs( (0,0))

print(min(ans))