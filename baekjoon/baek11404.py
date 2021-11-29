'''
백준 11404번
플로이드
'''


import sys
from collections import defaultdict


V = int(input())
E = int(input())

INF = 10**8
board = [[INF]*(V) for i in range(V)]
for i in range(V):
    board[i][i] = 0

for i in range(E):
    n1,n2,w = map(int, sys.stdin.readline().split())
    board[n1-1][n2-1] = min(w,board[n1-1][n2-1])

for i in range(V): # 거쳐가는 노드를 먼저 고정시키고 시작
    
    for j in range(V): #시작 노드
        for k in range(V): #도착 노드
            board[j][k] = min(board[j][k],board[j][i]+board[i][k])

for b in board:
    for v in b:
        if v>=INF:
            v=0
        print(v,end=' ')
    print()