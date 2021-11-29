'''
백준 1149번
RGB 거리
'''


def notI(i):
    li = [0,1,2]
    del li[i]
    return li

N = int(input())
dp = [ [0] * (N+5) for i in range(3) ]
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

for i in range(N):
    for t in range(3):
        notThis = notI(t)
        dp[t][i] = min(dp[notThis[0]][i-1],dp[notThis[1]][i-1]) + li[i][t]

print(min(dp[0][N-1],dp[1][N-1],dp[2][N-1]))    