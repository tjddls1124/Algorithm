'''
백준 1780번
종이의 개수
'''

N = int(input())
import sys

paper = []
for _ in range(N):
    paper.append(sys.stdin.readline().split())
res = {'-1':0,'0':0,"1":0}

def recur(i,j, leng):
    color = paper[i][j]

    if leng<=1:
        res[color] += 1
        return
    allSame = True
    for x in range(i,i+leng):
        for y in range(j,j+leng):
            if paper[x][y] != color:
                allSame = False
    if allSame:
        res[color] += 1
        return
    next_len = leng//3
    for x in range(3):
        for y in range(3):
            recur(i+next_len*x,j+next_len*y,next_len)

    return 

recur(0, 0, N)
for v in res.values():
    print(v)