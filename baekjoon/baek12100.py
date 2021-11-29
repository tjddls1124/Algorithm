'''
백준 12100
2048(Easy)

삼성기출, Easy라 써놨지만 쉽지 않음
'''

def isAvl(x=0,y=0):
    return  0<=x< N and 0<=y < N
    
def move(dir):
    global maxV
    if dir==1 or dir==2:
        delta = ()
        if dir==1:
            delta = (0,1,0)
        if dir==2:
            delta = (0,-1,N-1)
        dx = delta[0]
        dy = delta[1]
        st = delta[2]    
        for x in range(N):
            val = -1
            p_x = -1
            p_y = -1
            y=st
            containZero = False
            while isAvl(x,y):                
                if board[x][y]==0 and containZero==False:
                    containZero = (x,y)

                    continue
                if board[x][y] == 0:
                    x+=dx
                    y+=dy
                    continue
                
                if val==board[x][y]:
                    board[p_x][p_y] = val * 2
                    val = -1
                    board[x][y]=0
                    x,y=p_x, p_y
                    
                else:
                    if containZero!=False:
                        val = board[x][y]
                        board[x][y]=0
                        x,y=containZero
                        p_x,p_y = containZero
                        containZero= False
                        board[x][y] = val
                        
                    else:
                        val=board[x][y]
                        p_x=x
                        p_y=y
                    
                x+=dx
                y+=dy
    
        for b in board:
            maxV = max(maxV,max(b))
    
    if dir==3 or dir==4:
        delta = ()
        if dir==3:
            delta = (1,0,0)
        if dir==4:
            delta = (-1,0,N-1)
        dx = delta[0]
        dy = delta[1]
        st = delta[2]
            
        for y in range(N):
            val = -1
            p_x = -1
            p_y = -1
            x=st
            containZero = False
            while isAvl(x,y):                
                if board[x][y]==0 and containZero==False:
                    containZero = (x,y)

                    continue
                if board[x][y] == 0:
                    x+=dx
                    y+=dy
                    continue
                
                if val==board[x][y]:
                    board[p_x][p_y] = val * 2
                    val = -1
                    board[x][y]=0
                    x,y=p_x, p_y
                    
                else:
                    if containZero!=False:
                        val = board[x][y]
                        board[x][y]=0
                        x,y=containZero
                        p_x,p_y = containZero
                        containZero= False
                        board[x][y] = val
                        
                    else:
                        val=board[x][y]
                        p_x=x
                        p_y=y
                    
                x+=dx
                y+=dy
    
        for b in board:
            maxV = max(maxV,max(b))


board = []
N = int(input())
for i in range(N):
    board.append(list(map(int,input().split())))

maxV = 0
import copy
def dfs(depth):
    global board, maxV
    if depth == 5:
        return
    tmpBoard = copy.deepcopy(board) 
    for i in range(1,5):
        move(i)
        dfs(depth+1)
        board = copy.deepcopy(tmpBoard)

dfs(0)
print(maxV)