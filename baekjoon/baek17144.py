'''
백준 17144번

미세먼지 안녕!

simulation
'''
import copy
def fliter(room):
    tmp_r = copy.deepcopy(room)
    dir = -1
    for x,y in ac:
        x_offset = 1
        y_offset = 0
        i = x
        j = y
        while True:
            next_i = i+1*y_offset
            next_j = j+1*x_offset
            if next_j==C:
                x_offset = 0
                y_offset = 1 * dir
            if (next_i==-1 and dir==-1)or (next_i==R and dir==1):
                x_offset = -1
                y_offset =0
            if next_j ==-1:
                x_offset = 0
                y_offset = -1 * dir
            tmp_r[i+1*y_offset][j+1*x_offset] = room[i][j]
            
            i+= (1*y_offset)
            j+= (1*x_offset)
            if i==x and j==y:
                tmp_r[i][j] = -1
                break
            
        dir*=-1
    return tmp_r
    
def room_explode(room):
    tmp_r = [[0]*C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j]!=0 and room[i][j]!=-1:
                cnt = 0
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=x<R and 0<=y<C and room[x][y]!=-1:
                        tmp_r[x][y] += room[i][j]//5
                        cnt+=1
                tmp_r[i][j] += room[i][j] - (room[i][j]//5) * cnt
    return tmp_r

def explode_count(i,j):
    count = 0
    avl = [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    for x,y in avl:
        if 0<=x<R and 0<=y<C and room[x][y]!=-1:
            count+=1    
    
    return count
    
import sys
    
R,C,T = map(int,sys.stdin.readline().split())

room = []

for _ in range(R):
    room.append(list(map(int,sys.stdin.readline().split())))

ac = []
for i in range(R):
    for j in range(C):
        if room[i][j]==-1:
            ac.append((i,j))

tmp_room = copy.deepcopy(room)

for _ in range(T):
    tmp_room = room_explode(tmp_room)
    tmp_room = fliter(tmp_room)


from functools import reduce
print(reduce(lambda x,y: x+sum(y), tmp_room, 0) + 2)