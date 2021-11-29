'''
외판원 순회
dfs & memoization
'''

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

dp = [[INF] * (1<<16) for _ in range(N)]

visited = [0]*N
res = INF
st = 0

def visit(cur,b):
    if b==(1<<N)-1:
        return board[cur][st]

    if dp[cur][b] != INF :
        return dp[cur][b]
    
    r = INF
    for i in range(1,N):
        if visited[i]==0 and board[cur][i]!=INF:
            visited[i] = 1
            v = visit(i,b | 1<<i)
            if v +board[cur][i] < r:
                r = v + board[cur][i]
            visited[i] = 0
                
    dp[cur][b] = r
    return r

visited[st] = 1
print(visit(0,1))