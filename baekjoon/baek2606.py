'''
백준 2606번
바이러스

BFS
'''


N = int(input())
num = int(input())
dicts = {}
for i in range(num):
    a, b = map(int,input().split())
    if not a in dicts.keys():
        dicts[a] = []
    if not b in dicts.keys():
        dicts[b] = []
    dicts[a].append(b)
    dicts[b].append(a)
q = []    
q.append(1)
visited = [0] * (N+1)

def bfs():
    while len(q)!=0:
        p = q.pop()
        if visited[p]!=0:
            continue
        visited[p] = 1
        for i in dicts[p]:
            q.append(i)

bfs()
print(visited)
print(visited.count(1)-1)


    