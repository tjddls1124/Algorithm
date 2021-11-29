'''
백준 3190번 - 삼성 기출 문제
뱀
'''
import sys
import collections

EMPTY = 7

def move(board,cur_dir):
    head[0] += dirs[cur_dir][0]
    head[1] += dirs[cur_dir][1] 
    if  0 < head[0] <= N and 0 < head[1] <= N and (board[head[0]][head[1]]==EMPTY or board[head[0]][head[1]]=='A'):
        
        if not board[head[0]][head[1]] == 'A':
            tail_dir = board[tail[0]][tail[1]]
            board[tail[0]][tail[1]] = EMPTY
            tail[0] += dirs[tail_dir][0]
            tail[1] += dirs[tail_dir][1]            
        board[head[0]][head[1]] = cur_dir
        
        return True
    else:
        return False
    
    
N = int(input()) #보드의 크기 
K = int(input()) #사과의 개수

board = [[EMPTY]*(N+1) for _ in range(N+1)]
apples = []
for _ in range(K):
    apples.append(tuple(map(int,sys.stdin.readline().split())))

for apple in apples:
    board[apple[0]][apple[1]] = 'A'
    
L = int(input())

movements = collections.deque()

for _ in range(L):
    movements.append(tuple(sys.stdin.readline().split()))

# R D L U
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

head = [1,1]
tail = [1,1]
board[1][1] = 0
cur_dir = 0
cnt = 0
INF = 10**8
movements.append((INF,'C'))
while movements:
    t, direc = movements.popleft()
    t = int(t)
    while cnt < t:
        cnt += 1
        if not move(board,cur_dir):
            print(cnt)
            sys.exit()
    if direc == 'D':
        cur_dir+=1
        cur_dir%=4
    if direc == 'L':
        cur_dir-=1
        cur_dir%=4
        
    board[head[0]][head[1]] = cur_dir
        
print(cnt-1)
    
    

            
        
        
    