'''
백준 2667번
단지번호 붙이기

DFS
'''
import sys
sys.setrecursionlimit(10**4)

N = int(input())
ans = 0
board = []
for i in range(N):
    board.append(input())
visited = [ [0]*N for i in range(N) ]

def dfs(pos,color):
    global ans,visited
    
    x = pos[0]
    y = pos[1]
    if not isAvl(pos) or board[x][y] == '0':
        return
    
    if visited[x][y] != 0:
        return
    
    if color ==0 :
        ans+=1
        visited[x][y] = ans
        color = ans
    else:
        visited[x][y] = ans

    
    positions = [ (x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    
    for p in positions:
        dfs(p,color)

def isAvl(pos):
    x = pos[0]
    y = pos[1]
    if 0<= x < N and 0 <= y < N:
        return True
    return False

for i,val in enumerate(board):
    for j in range(len(val)):
        dfs((i,j), 0)
print(ans)

ans = [0 for i in range(N**2)]
for v in visited:
    for c in v:
        if c!= 0:
            ans[c] += 1
for a in sorted(ans):
    if a!= 0 :
        print(a)