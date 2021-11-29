'''
백준 7579번
앱

'''
import sys

N, M = map(int,input().split())

mem_arr = list(map(int,input().split()))
cost_arr = list(map(int,input().split()))
INF = 10**12
weight_arr = [0] * N
dp = [INF] * (10000000+1)
for i in range(N):
    if cost_arr[i] != 0 : 
        weight_arr[i] = (mem_arr[i]/cost_arr[i] , mem_arr[i], cost_arr[i])
    else:
        weight_arr[i] = (INF,mem_arr[i],cost_arr[i])
weight_arr = sorted(weight_arr,reverse=True)
for i in range(N):    
    w,m,c = weight_arr[i]
    minv = INF
    for j in reversed(range(M+1)):
        if dp[j] == INF:
            continue
        t = m+j
        if m + j > M:
            t = M
        dp[t] =  min(dp[t], dp[j] + c )
        dp[j] = minv = min(dp[j],minv)
         
    dp[m] = min(dp[m],c)
print(min(dp[M:]))
