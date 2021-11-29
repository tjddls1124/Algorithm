'''
백준 1987번
알파벳

bfs
'''


import sys

def isAvl(x,y,acc):
    if 0<=x<N and 0<=y<M and not(board[x][y] in acc):
        return True
    return False
'''
def dfs(x,y,acc):
    global maxV
    if maxV < len(acc):
        maxV = len(acc)
        
    if len(acc)==26:
        return
    
    positions= [(x+1,y,acc),(x-1,y,acc),(x,y+1,acc),(x,y-1,acc)]
    for pos in positions:
        if isAvl(pos[0], pos[1], pos[2]):
            dfs(pos[0],pos[1],pos[2]+board[pos[0]][pos[1]])
            sets.add((pos[0],pos[1],pos[2]+board[pos[0]][pos[1]]))
'''
import sys

N,M = map(int,sys.stdin.readline().split())
maxV = 0

import queue
q = set()
board = []
visited = [[0] * M for i in range(N)]

for i in range(N):
    board.append(sys.stdin.readline())


q.add((0,0,board[0][0]))
while(len(q)!=0):
    pop = q.pop()
    x = pop[0]
    y = pop[1]
    acc = pop[2]
    if maxV < len(acc):
        maxV = len(acc)

    positions= [(x+1,y,acc),(x-1,y,acc),(x,y+1,acc),(x,y-1,acc)]
    for pos in positions:
        if isAvl(pos[0], pos[1], pos[2]):
            tup = (pos[0],pos[1],pos[2]+board[pos[0]][pos[1]])
            if not tup in q:
                q.add(tup)
print(maxV)
    


