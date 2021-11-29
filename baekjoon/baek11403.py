'''
백준 11403번
경로 찾기
'''

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
    
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            for t in range(N):
                if board[j][t] == 1:
                    board[i][t] = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            for t in range(N):
                if board[j][t] == 1:
                    board[i][t] = 1
                    
for b in board:
    for v in b:
        print(v,end=' ')
    print()