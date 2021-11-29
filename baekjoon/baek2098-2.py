
import sys

N = int(sys.stdin.readline())
board = []
INF = 10**9
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if board[i][j] == 0:
            board[i][j] = INF

dp = [[INF] * (2**16) for _ in range(N)]

visited = [0]*N
res = INF
st = 0

def visit(cur,acc,b):
    global res
    if b==(1<<N)-1:
        if res > acc+board[cur][st]:
            res = acc+board[cur][st]
        return
    if dp[cur][b] <= acc:
        print("a")
        return
    dp[cur][b] = acc
    
    for i in range(1,N):
        if visited[i]==0 and board[cur][i]!=INF:
            visited[i] = 1
            visit(i,acc+board[cur][i],b | 1<<i )
            visited[i] = 0

visited[st] = 1
visit(0,0,1)

print(res)