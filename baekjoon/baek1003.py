'''
백준 1003번
피보나치 함수
'''

T = int(input())
lis= []

for i in range(T):
    lis.append(int(input()))
n = max(lis)
dp = [(0,0)] * (n+1)
dp[0] = (1,0)
dp[1] = (0,1)

for i in range(n+1):
    if i ==0 or i ==1:
        continue
    dp[i] = (dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1])
    
for i in lis:
    print(dp[i][0], dp[i][1])
# n : n-1 + n-2
