'''
백준 12852번
1로 만들기2
'''
from copy import deepcopy
import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())
INF = 10 ** 6
    
dp = [[] for _ in range(N+1)]
q = deque()

def bfs():
    q.append(N)
    dp[N].append(N)
    while True:
        num = q.pop()
        if num == 1:
            break
        
        nexts = []
        if num%3==0:
            nexts.append(num//3)
        if num%2==0:
            nexts.append(num//2)
        nexts.append(num-1)

        for n in nexts:
            if n < 1:
                continue
            if len(dp[n])!=0 and len(dp[n]) <= len(dp[num])+1:
                continue
            q.appendleft(n)
            copyed = deepcopy(dp[num])
            copyed.append(n)
            dp[n] = copyed
    
    

bfs()
print(len(dp[1])-1)
for v in dp[1]:
    print(v,end=' ')