import sys

N ,B = map(int,sys.stdin.readline().split())

def sqmult(a,b):
    if b==1:
        return a
    
    t = sqmult(a,b//2)
    if b%2==0:
        return mult(t ,t)
    else:
        return mult(mult(t ,t) , a)
    
def mult(a,b):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N):
                s += a[i][k] * b[k][j]
            res[i][j] = s % 1000
    return res
    
mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))
    
for v in sqmult(mat,B):
    for t in v:
        print(t%1000,end=' ')
    print()