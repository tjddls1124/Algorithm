'''
A->B
'''
import collections

q = collections.deque()

a,b = map(int,input().split())

q.append((a,0))
while q:
    p,depth = q.popleft()
    if p == b:
        print(depth+1)
        exit()
    
    nexts = [p*2, int(str(p)+"1")]
    for n in nexts:
        if n > b:
            continue
        q.append([n,depth+1])

print("-1")