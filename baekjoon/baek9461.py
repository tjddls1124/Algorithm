'''
백준 9461번
파도반 수열

'''

N = int(input())
arr = []
maxV = 0
for i in range(N):
    inp = int(input())
    maxV = max(maxV, inp)
    arr.append(inp)
    
dp = [0] * (maxV+6)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5,maxV+1):
    dp[i] = dp[i-1]+ dp[i-5]

for a in arr:
    print(dp[a])