'''
백준 11726번
2xn 타일링

DP
'''

mod = 10007

n = int(input())
dp = [0] * (n+5)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
