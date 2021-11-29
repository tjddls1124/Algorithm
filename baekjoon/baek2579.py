'''
백준 2579번
계단오르기

DP

'''

N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))    

def dfs(i, val, conti):
    if i>=len(stairs):
        return
    val = val+stairs[i]

    if conti == 2:
        return
    
    if i==len(stairs)-1:
        res.append(val)
        return

    
    
    dfs(i+1,val,conti=conti+1)
    dfs(i+2,val,conti=0)

dp = [[0] * (N+5) for i in range(2)]
dp[1][0] = 0
dp[0][0] = stairs[0]
for i in range(1,N):
    dp[1][i] = dp[0][i-1] + stairs[i]
    dp[0][i] = max(dp[1][i-2],dp[0][i-2]) + stairs[i]
    
print( max(dp[0][N-1],dp[1][N-1]) ) 