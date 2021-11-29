'''
게임
'''
import sys
sys.setrecursionlimit(10**8)

N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline())

visited = [[0]*M for i in range(N)]
dp = [[0]*M for i in range(N)]

INF = 10**10

def isAvl(x,y,depth):
    return 0<=x<N and 0<=y<M and board[x][y]!='H' and depth > dp[x][y]

def dfs(x,y,depth):
    num = int(board[x][y])
    positions = [(x+num,y,depth),(x-num,y,depth),(x,y+num,depth),(x,y-num,depth)]
        
    arr = []
    for pos in positions:
        if isAvl(pos[0],pos[1],pos[2]+1):
            if visited[pos[0]][pos[1]]==1:
                return INF
            dp[pos[0]][pos[1]] = pos[2]+1
            visited[pos[0]][pos[1]] = 1
            arr.append(dfs(pos[0],pos[1],depth+1))
            visited[pos[0]][pos[1]] = 0
    if len(arr)==0:
        return depth
    
    
    return max(arr)

res = dfs(0,0,1)
if res!=INF:
    print(res)
else:
    print("-1")