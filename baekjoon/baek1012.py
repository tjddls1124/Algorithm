'''
백준 1012
유기농배추

dfs / max recursionlimit 설정할 것
'''


import sys
sys.setrecursionlimit(2600) ## point!!!

def solution(board,N,M):
    def isAvl(x,y):
        if 0<= x < N and 0<= y < M:
            return True
        return False
                
    
    def dfs(pos,color,prev, crossC=True):
        nonlocal ans 
        
        x = pos[0]
        y = pos[1]
        if not isAvl(x, y):
            return
        cur = board[x][y]
        
        if visited[x][y]!=0:
            return
        
        visited[x][y] = -1
        
        if board[x][y]!=1:
            return
        
        if color == 0 :
            ans += 1
            visited[x][y] = ans
        

        
            
        positions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        
        for pos in positions:
            dfs(pos,ans,cur)
           
              
    visited = [ [0]*M for i in range(N) ]
    ans = 0   
    answer = []
    for i in range(N):
        for j in range(len(board[0])):
            if board[i][j]==1:
                dfs((i,j),0,board[i][j])
    #for v in visited:
    #    print(v)
    print(ans)
    
T = int(input())
for t in range(T):
    M,N,K = map(int, input().split())
    board = [[0]*M for i in range(N)]
    for i in range(K):
        x,y = map(int, input().split())
        board[y][x] = 1
    
    #print("\n"*3)
    solution(board,N,M)
