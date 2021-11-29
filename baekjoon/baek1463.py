'''
백준 1463번
1로 만들기

DP
'''
import sys
sys.setrecursionlimit(10**5)
a = int(input())
dp = [0] * (a+1)
dp[1] = 0

for i in range(1,a+1):
    r1 = 10**6
    r2 = 10**6
    r3 = 10**6
    
    if i%3==0:
        r1 = dp[i//3]
    if i%2 ==0:
        r2 = dp[i//2]
    
    r3 = dp[i-1]
        
    dp[i] = min([r1,r2,r3]) + 1
    

print(dp[a]-1)
