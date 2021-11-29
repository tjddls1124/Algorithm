from collections import deque

def solution(board):
    answer = 0
    return bfs(board)
    


ROWDIR = 0
COLDIR = 1

def bfs(board):
    q = deque()
    start = [0,1,ROWDIR,0]
    q.append(start)
    s = set()
    
    while True:
        cur = q.popleft()
        if cur[0] == len(board)-1 and cur[1] == len(board)-1:
            return cur[3]
        
        #get movable pos
        movList = getMovalbePos(cur, board, len(board))
        #get spinable pos
        spinList = getSpinablePos(cur, board, len(board))
        

        for m in movList:
            if getString(m) in s:
                continue
            s.add(getString(m))
            q.append(m)
        for m in spinList:
            if getString(m) in s:
                continue
            s.add(getString(m))
            q.append(m)
            
        
def getMovalbePos(cur,board,N):
    arr = []
    res = []
    x = cur[0]
    y = cur[1]
    dir = cur[2]
    cnt = cur[3]
    
    #right
    arr.append([x-1,y,dir,cnt+1])
    #left
    arr.append([x+1,y,dir,cnt+1])
    #up
    arr.append([x,y-1,dir,cnt+1]) 
    #down
    arr.append([x,y+1,dir,cnt+1])
    
    for cd in arr:
        if isAval(getPos(cd),board,N):
            res.append(cd)
   
    return res
    
def getSpinablePos(cur,board,N):
    x = cur[0]
    y = cur[1]
    dir = cur[2]
    move = cur[3]
    arr = []
    res = []
    
    #방향 플립
    direc = (dir+1) % 2
    if direc == COLDIR:
        arr.append([x,y,direc,move+1])
        arr.append([x,y-1,direc,move+1])
        arr.append([x+1,y,direc,move+1])
        arr.append([x+1,y-1,direc,move+1])
    else:
        arr.append([x,y,direc,move+1])
        arr.append([x-1,y,direc,move+1])
        arr.append([x,y+1,direc,move+1])
        arr.append([x-1,y+1,direc,move+1])
    for cd in arr:
        pos = getSpinPos(cur,cd)
        if isPointAval(pos[0],pos[1],board,N) and board[pos[0]][pos[1]] != 1 and isAval(getPos(cd), board, N):
            res.append(cd)
    return res
    
def getSpinPos(cur,next):
    x1,y1,x2,y2 = getPos(cur)
    x3,y3,x4,y4 = getPos(next)
    
    s = set([(x1,y1),(x2,y2),(x3,y3),(x4,y4)])
    x = 0
    y = 0
    for i in s:
        x ^= i[0]
        y ^= i[1]
    
    
    return [x,y]
    
    
def getPos(cur):
    x1 = cur[0]
    y1 = cur[1]    
    if cur[2] == COLDIR:
        x2 = x1-1
        y2 = y1 
    else:
        x2 = x1
        y2 = y1-1
    
    return x1,y1,x2,y2

def isPointAval(x,y, board,N):
    return (x < N) and (y < N) and (x >= 0) and (y >= 0 ) and (board[x][y] != 1)

def isAval(cds, board,N):
    x1,y1,x2,y2 = cds
    return (x1 < N) and (y1 < N) and (x2 <N)and(y2 <N) and(x1 >= 0)and(y1 >= 0 )and(x2 >= 0)and(y2 >= 0) and (board[x1][y1] != 1) and (board[x2][y2] != 1)




def getString(cur):
    return (cur[0],cur[1],cur[2])



if __name__ == '__main__':
    print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
    