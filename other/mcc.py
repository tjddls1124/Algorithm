'''
월간 코드 챌린지 9월
'''
import sys
sys.setrecursionlimit(10**6)

def solution1(numbers):
    answer = 0
    
    for number in range(0,10):
        if number in set(numbers):
            continue
        answer+= number
        
    
    return answer


visited = []
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
def solution(grid):
    global visited
    visited = []    
    for _ in range(len(grid)):
        visited.append([[0]*4 for _ in range(len(grid[0]))])
        
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            for dir in range(4):
                travel(i,j,dir,grid[i][j],0, grid)

    return sorted(color)
color = []

def mod(i,n):
    return (i+n)%n
 
def travel(i,j,dir,gr,res, grid):
    
    if visited[i][j][dir] != 0 :
        if res!=0:
            color.append(res)
        return
    visited[i][j][dir] = 1
    
    if dir==DOWN:
        i+=1
    if dir==UP:
        i-=1
    if dir==RIGHT:
        j+=1
    if dir==LEFT:
        j-=1
    
    res+=1
    if not 0<=i<len(grid):
        i = mod(i,len(grid))
    if not 0<=j<len(grid[0]):
        j = mod(j,len(grid[0]))

    if grid[i][j] == 'S':
        new_dir = dir
    if grid[i][j] == 'R':
        if dir==DOWN:
            new_dir = LEFT
        if dir==UP:
            new_dir = RIGHT
        if dir==RIGHT:
            new_dir = DOWN        
        if dir==LEFT:
            new_dir = UP
    
    if grid[i][j] == 'L':
        if dir==DOWN:
            new_dir = RIGHT
        if dir==UP:
            new_dir = LEFT
        if dir==RIGHT:
            new_dir = UP        
        if dir==LEFT:
            new_dir = DOWN
    travel(i,j,new_dir,grid[i][j],res, grid)
    



import sys
N = 0
def solution(a, b, g, s, w, t):
    global N
    N = len(g)    
    bsearch(0, 10**15, a, b, g, s, w, t)
    return maxTime

def bsearch(low,high,a,b,g,s,w,t):
    global maxTime
    mid = (low+high)//2
    
    if low>high:
        return
    if canConst(a, b, g, s, w, t, mid):
        maxTime = mid
        bsearch(low, mid-1, a, b, g, s, w, t)
    else:
        bsearch(mid+1, high, a, b, g, s, w, t)
    
    
    
def canConst(gold,sliver,g,s,w,t,time):
    res = (0,0)
    max_v = 0
    for i in range(N):
        if time > t[i]:
            count = (time - t[i]) // (t[i]*2) + 1
            max_v += min(w[i]*count,g[i]+s[i])
            res = ( res[0] + min(g[i], w[i] * count) ,res[1] + min(w[i]*count,s[i]) )
    if max_v < (gold+sliver):
        return False
    if res[0] <  gold or res[1] < sliver:
        return False
    
    return True

if __name__ == '__main__':
    print(solution(60, 60, [60,30,50], [60,30,10], [20,10,10], [1,1,2]))