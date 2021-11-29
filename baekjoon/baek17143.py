'''
낚시왕
'''

import sys

R,C,M = map(int,sys.stdin.readline().split())
sharks = []

UP = 1
DOWN = 2
RIGHT =3 
LEFT = 4

def changeDir(dir):
    if dir==UP:
        return DOWN
    if dir==DOWN:
        return UP
    if dir==LEFT:
        return RIGHT
    if dir==RIGHT:
        return LEFT
    
def nextPos(r,c,sp,dir,size):
    if dir==UP:
        r-=sp
    if dir==DOWN:
        r+=sp
    if dir==RIGHT:
        c+=sp
    if dir==LEFT:
        c-=sp
    
    nd = dir
    if r < 0 or c < 0 :
        r = abs(r)
        c = abs(c)
        nd = changeDir(nd)
    if r >= R:
        if  ( r // (R-1) ) % 2== 1:
            nd = changeDir(nd)
            r = R -1 - r % (R-1)
        else:
            r = r % (R-1)    
    if c >= C:
        if  ( c // (C-1) ) % 2== 1:
            nd = changeDir(nd)
            c = C-1 - c % (C-1)
        else:
            c = c % (C-1)
    
    return r,c , nd
    

for _ in range(M):
    # r,c speed, dir , size
    sharks.append(list(map(int,sys.stdin.readline().split())))

for shark in sharks:
    shark[0] -=1
    shark[1] -=1

res = 0
catched = []

pos = 0
for t in range(C):
    min_r = 1000
    target = -1    
    for i, shark in enumerate(sharks):
        if i in catched:
            continue
        if shark[1] == pos:
            if min_r > shark[0]:
                min_r = shark[0]
                target = i
        
    if target != -1:  
        catched.append(target)      
        res+= sharks[target][4]
            
    acuarium = [[0] * C for _ in range(R)]
    for i, shark in enumerate(sharks):
        if i in catched:
            continue
        size = shark[4]
        nr, nc , nd = nextPos(*shark)
        if acuarium[nr][nc] != 0:
            if size < acuarium[nr][nc][1]:
                catched.append(i)
                continue
            else:
                catched.append(acuarium[nr][nc][0])
        shark[0] = nr
        shark[1] = nc 
        shark[3] = nd
        acuarium[nr][nc] = (i,size)
    pos+=1

    
print(res)