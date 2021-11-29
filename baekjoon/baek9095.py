'''
백준 9095번 문제
1,2,3 더하기

DP
'''

T = int(input())

arr= []
for i in range(T):
    arr.append(int(input()))

ma = max(arr)
dp = [0] * (ma+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,ma+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for i in arr:
    print(dp[i])