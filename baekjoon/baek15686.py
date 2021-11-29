'''
백준 15686번
치킨배달
'''



def getDist(ch,ho):
    return abs(ch[0]-ho[0]) + abs(ch[1] -ho[1])

N,M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))

chicks = []
houses = []

from itertools import combinations

for i in range(N):
    for j in range(N):
        if board[i][j]== 2:
            chicks.append((i,j))
        if board[i][j] == 1:
            houses.append((i,j))
res = 10**6
for chCase in list(combinations(chicks, M)):
    cityDist = 0
    for ho in houses:
        chDist = 10**6
        for ch in chCase:
            chDist = min(chDist,getDist(ch, ho))
        cityDist += chDist
    res = min(res,cityDist)    
print(res)