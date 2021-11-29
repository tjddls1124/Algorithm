'''
백준 1260번
DFS 와 BFS
'''


from collections import deque
N,M,V = map(int,input().split())

di = {}
for i in range(M):
    x, y = map(int, input().split())
    if not x in di.keys() :
        di[x] = []
    if not y in di.keys() :
        di[y] = []
    di[y].append(x)
    di[x].append(y)


q =  deque()


def visit(isDFS=False):
    ans = ""
    
    for key in di.keys():
        if isDFS:
            di[key] = sorted(di[key],key=lambda x: -x)
        if not isDFS:
            di[key] = sorted(di[key])
        
    visited = [0] * (N+1)
    q.append(V)
        
    while(len(q)!=0):
        
        if isDFS:
            v=q.pop()
        else:
            v = q.popleft()
            
        if visited[v]!=0:
            continue
        ans += f"{v}" + " "
        visited[v] = 1
        
        if not v in di.keys():
            break
        
        for node in di[v]:
            if isDFS:
                q.append(node)
            else:
                q.append(node)
    print(ans)

visit(True)
visit()