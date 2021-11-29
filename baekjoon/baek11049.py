'''
행렬 곱셈 순서
'''

import sys


INF = 987654321

N = int(input())
ma = []
dp = [[INF] * N for _ in range(N)]

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    ma.append((a,b))
    dp[i][i] = 0
for i in range(N-1):
    dp[i][i+1] = ma[i][0] * ma[i][1] * ma[i+1][1]

for diag in range(1,N):
    for i in range(N-diag):
        j = i + diag
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + ma[i][0] * ma[k][1] * ma[j][1] ) 

print(dp[0][N-1])
