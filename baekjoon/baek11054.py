'''
백준 11053
가징 긴 바이토닉 부분수열
'''

N = int(input())

arr = list(map(int,input().split()))
dp = [0] * N 
dp_r = [0] * N

for i in range(0,N):
    dp[i] = 1
    for j in range(0,i+1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1,dp[i])
      
arr.reverse()
for i in range(0,N):
    dp_r[i] = 1
    for j in range(0,i+1):
        if arr[j] < arr[i]:
            dp_r[i] = max(dp_r[j]+1,dp_r[i])
dp_r.reverse()
ma = 0
for i in range(N):
    ma = max(ma, dp[i] + dp_r[i])
print(ma-1)