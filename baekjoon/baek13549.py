'''
백준 13549번
숨바꼭질 2
'''

from collections import deque

q = deque()
N, K = map(int,input().split())
MAX = 100000
q.append((N,0))
INF = 0
dp = [INF] * int( 1.5 * MAX + 1)
while q:
    cur, depth = q.popleft()
    if cur==K:
        print(depth)
        break
    if dp[cur] != INF:
        continue
    dp[cur] = depth
    positions = [cur*2,cur+1,cur-1]
    for po in positions:
        if po < 0 or po > MAX*(1.5) :
            continue
        if dp[po]!=0:
            continue
        if po == cur*2 and po!=0:
            q.appendleft((po,depth))
        else:
            q.append((po,depth+1))
    