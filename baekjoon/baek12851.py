
N, K = map(int,input().split())

import collections
q = collections.deque()

arr = [100000] * 100001

q.append((N,0))
res = 100000
cnt = 0

while q:
    p,depth = q.popleft()
    if depth <= arr[p]:
        arr[p] = depth
    else:
        continue
    
    pos = [2*p, p+1 , p-1]
    if depth == res+1:
        break
    
    if p == K:
        res = depth
        cnt+=1
        
    
    for x in pos:
        if 0 <= x <= 100000:
            q.append((x,depth+1))

print(res,cnt)
