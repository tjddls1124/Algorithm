from collections import deque

T = int(input())
for i in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    
    q = list(map(int,input().split()))
    idx_q = [t for t in range(N)]

    count = 0
    while len(q)!=0:
        p = q[0]
        del q[0]
        
        idx = idx_q[0]
        del idx_q[0]
        
        if len(q)!=0 and p < max(q):
            q.append(p)
            idx_q.append(idx)
        else:
            #print
            count+=1
            if idx==M:
                print(count)
                break

        
