## 영역나누기

'''
 [
 [0 1 0 1 0]
 [0 1 0 1 1]
 [1 1 0 0 0]
 [0 0 1 1 1]
 [0 0 1 0 0]
 ]
'''

board = []


def solution(board):
    def isAvl(x,y):
        if 0<= x < N and 0<= y < N:
            return True
        return False
                
    
    def isConnect(cur,prev):
        if cur==prev:
            return True
        return False
    
    def dfs(pos,color,prev, crossC=True):
        nonlocal ans 
        
        x = pos[0]
        y = pos[1]
        if not isAvl(x, y):
            return
        cur = board[x][y]
        if not isConnect(cur, prev):
            return
        if visited[x][y] != 0:
            return
        
        if color == 0 and visited[x][y]==0:
            ans += 1
        visited[x][y] = ans
        
            
        positions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
       
        if not crossC:
            positions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),
                         (x+1,y+1),(x+1,y-1),(x-1,y-1),(x-1,y+1)]
       
        for pos in positions:
            dfs(pos,ans,cur,crossC)
                

    N = len(board)
    visited = [ [0]*N for i in range(N) ]
    ans = 0   
    answer = []
    for i in range(N):
        for j in range(len(board[0])):
            dfs((i,j),0,board[i][j])
    answer.append(ans)
    
    visited = [ [0]*N for i in range(N) ]
    ans = 0
    
    for i in range(N):
        for j in range(len(board[0])):
            dfs((i,j),0,board[i][j],False)
            
    answer.append(ans)
    
    for v in visited:
        print(v)

    print(answer)
    
        
        

    
    
    
if __name__ == '__main__':
    a = solution([
 [0,1, 0, 1 ,0],
 [0,1, 0, 1 ,1],
 [1,1, 0, 0, 0],
 [0,0 ,1, 1, 1],
 [0,0, 1, 0, 0],
 ])
    print(a)