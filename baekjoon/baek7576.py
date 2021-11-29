'''
백준 7576번
토마토

BFS
'''
import collections
import sys

def main():
    M , N = map(int, input().split())
    maxV = -1
    board = []
    visited = [[0] * M for i in range(N)]
    
    for i in range(N):
        board.append( list(map( int, sys.stdin.readline().split()  )) )
    
    q = collections.deque()
    def isAvl(x,y):
        if 0 <= x < N and 0<= y < M:
            if board[x][y] == -1:
                return False
            return True
        
        return False
    ans = -1
    def bfs():
        nonlocal maxV
        while len(q)!=0:
            p = q.popleft()   
            x = p[0]
            y = p[1]
            
            maxV = max(maxV,p[2])
            positions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for pos in positions:
                if isAvl(pos[0], pos[1]):
                    if visited[pos[0]][pos[1]] != 0:
                        continue
                    q.append((pos[0],pos[1],p[2]+1))
                    visited[pos[0]][pos[1]] = p[2]+1

    allDone = True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1:
                visited[i][j] = -1
            if board[i][j] == 1:
                visited[i][j] = 'P'
                q.append((i,j,0))
            if board[i][j] == 0:
                allDone = False
    if allDone:
        print("0")   
        return
    bfs()
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] == 0:
                maxV = -1
    print(maxV)
   
if __name__ == '__main__':
    main()
    