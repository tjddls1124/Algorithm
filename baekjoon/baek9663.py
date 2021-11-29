'''
백준 9663
N Queen


'''

def isAvl(i,j):
    if 0<= i < N and 0 <= j < N:
        return True
    return False
def setLoop(i,j,i_p,j_p,arr):
    while True:
        i+=i_p
        j+=j_p
        if not isAvl(i,j):
            break
        if board[i][j] == 0:
            board[i][j] = 1
            arr.append((i,j))
            
def setBoard(i,j):
    arr = []
    dx = [0,0,1,-1,1, -1,1,-1]
    dy = [1,-1,0,0,-1,1,1,-1]
    for t in range(len(dx)):
        setLoop(i, j, dx[t], dy[t],arr)
    return arr

def dfs(i,j):
    global count
    if j==N-1:
        count+=1
        return
    
    li = setBoard(i, j)
    
    for t in range(N):
        if isAvl(t,j+1) and board[t][j+1]==0:
            dfs(t,j+1)
    for tup in li:
        board[tup[0]][tup[1]] = 0
        
    return    


N = int(input())
board = [[0] * N for i in range(N)]

count = 0

ans = 0
for i in range(N//2):
    dfs(i,0)

ans += count * 2
count = 0
if N%2 != 0 :
    dfs(N//2,0)
ans += count

print(ans)
