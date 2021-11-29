def solution1(seat):
    answer = 0
    cors = []
    Ms = []
    Ns = [] 
    
    for i,se in enumerate(seat):
        for j,t in enumerate(se):
            if t == 'C':
                cors.append((i,j))    
            if t =='M':
                Ms.append((i,j))
            if t == 'N':
                Ns.append((i,j))
    mset = set()
    for cor in cors:
        for m in Ms:
            if manhatt(cor,m) <= 3:
                mset.append(m)
        for n in Ns:
            if manhatt(cor,n) <=2:
                mset.append(n)
    
    return len(mset)

def manhatt(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


INF = 100
maps = [[INF]* 13 for _ in range(13)] 

nodes = [
    (1,2),(1,3),
    (2,3),
    (3,4),(3,5),
    (4,5),
    (5,6),(5,7),
    (6,7),
    (7,8),
    (8,9),(8,10),
    (9,10),
    (10,11),(10,12),
    (11,12)]
def solution(music):
    for n in nodes:
        maps[n[0]][n[1]] = 1
        maps[n[1]][n[0]] = 1
    for i in range(13):
        maps[i][i] = 0
    
    for k in range(13):
        for i in range(13):
            for j in range(13):
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j] ) 
    
    st = 1
    ans = 0
    for m in music:
        ans += maps[st][m]
        st = m
    
    print(ans)
    return ans

from collections import defaultdict, deque

def solution(n, edges):
    dic = defaultdict(list)
    
    answer = 0
    K = 0
    
    visited = [False] * n
    
    for edge in edges:
        dic[edge[0]].append(edge[1])
        dic[edge[1]].append(edge[0])

    q = deque()
    q.append((0,0))
    visited[0] = True
    cnt = 0
    
    cur_depth = 1
    while q:
        p,depth = q.popleft()
        cnt+=1
        if cnt>=3:
            if cur_depth < depth:
                K+=1
                cur_depth= depth
            K+=1
            answer+=K
        print(answer,K)
                
        for n in dic[p]:
            if visited[n]:
                continue
            visited[n] = True
            
            q.append((n,depth+1))
                        
    return answer * 2

    



if __name__ == '__main__':
    solution(5,[[0,1],[0,2],[1,3],[1,4]])
    