answer = []
arr = []
M = 0

def solution(lengths):
    global answer,arr,M
    arr = list(reversed(lengths))
    M = 1
    for l in lengths:
        M*=l
    answer = [[0] * M for _ in range(M)]
    snail(1, 0, 0,M, 0)
    return answer

def snail(st_val,st_x,st_y,mul,i):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    l = mul//arr[i]
    x= st_x
    y = st_y
    val = st_val
    dir = 0
    while  True:
        if not i==len(arr)-1:
            snail(val,x,y,l,i+1)
        else:
            draw_snail(val, x, y,mul)
            break
        if val >= st_val + mul*mul -l*l:
            break
        while True:
            nx = x+dx[dir]*l
            ny = y+dy[dir]*l
            if 0 <= nx < st_x + mul and 0<=ny< st_y + mul and answer[nx][ny]== 0:
                val+=l*l
                x = nx
                y =ny
                break
            else:
                dir = (dir+1)%4
    return


def draw_snail(st_val, st_x,st_y, l):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x= st_x
    y = st_y
    val = st_val
    dir = 0
    while  True:
        answer[x][y] = val
        if val >= st_val + l*l - 1:
            break
        nx = x+dx[dir]
        ny = y+dy[dir]
        if st_x <= nx < st_x + l and st_y <=ny< st_y + l and answer[nx][ny]== 0:
            val+=1
            x = nx
            y =ny
        else:
            dir = (dir+1)%4
            continue
    return
    

if __name__ == '__main__':
    for v in solution([3,2,2]):
        print(v)
    