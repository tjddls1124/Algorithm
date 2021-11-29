'''
백준 10026번
적록색약
'''

N = int(input())
picture = []
for _ in range(N):
    picture.append(input())

M = len(picture[0])

from collections import deque
q = deque()

def isSame(col1,col2,RG):
    if col1==col2:
        return True
    if RG :
        if 'R' in (col1,col2) and 'G' in (col1,col2):
            return True
    return False

count = 0
def bfs(i,j,color,RG):
    global count
    if visited[i][j]:
        return
    count+=1
    q.append((i,j))
    while q:
        i,j = q.popleft()
        points = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for point in points:
            x = point[0]
            y = point[1]
            if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                if isSame(color, picture[x][y], RG):
                    visited[x][y] = True
                    q.append((x,y))
                    
visited = []
def result(RG):
    global visited, count
    visited = [[False]*M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            bfs(i,j,picture[i][j],RG)
    print(count)

result(False)
result(True)