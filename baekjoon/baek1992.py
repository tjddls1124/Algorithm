'''
백준 1992번
쿼드트리
recursion
'''

maps = []
arr = []

def recur(i,j,len):
    if len == 1:
        return maps[i][j]
    
    color = maps[i][j]
    allQuard = True
    for x in range(i,i+len):
        for y in range(j,j+len):
            if maps[x][y] != color:
                allQuard = False
                break
    if allQuard:
        return color
    
    new_len = len//2
    return "(" + recur(i,j,new_len) + recur(i,j+new_len,new_len) + recur(i+new_len,j,new_len) + recur(i+new_len,j+new_len,new_len) + ")"           

N = int(input())
maps = []
for _ in range(N):
    maps.append(input())

print(maps[:2][:])

#print(recur(0, 0, N))