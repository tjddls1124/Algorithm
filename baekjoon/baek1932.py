'''
백준 1932번
정수 삼각형
'''

N = int(input())
tri = []
dp = [ [0] * (N+2) for i in range(N)]
for i in range(N):
    tri.append(list(map(int,input().split())))
for i in range(N):
    for j in range(i+1):
        dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1]) + tri[i][j]
print(max(dp[N-1]))