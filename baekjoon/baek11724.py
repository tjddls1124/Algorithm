import sys

def main():    
    N, M = map(int, input().split())
    arr = [0] * (N+1)
    for i in range(M):
        a,b = map(int,sys.stdin.readline().split())

        if arr[a]==0 and arr[b]==0:
            arr[a] = [a]
            arr[b] = arr[a]
            continue
        if arr[a] == 0:
            arr[a] = arr[b]
            continue
        
        if arr[b] == 0:
            arr[b] = arr[a]
            continue
        
        arr[a][0] = arr[b][0]
        
    res = set()
    others = 0
    for i in range(1,len(arr)):
        if arr[i] != 0:
            res.add(arr[i][0])
        else:
            others+=1
        
    print(len(res)+others)

if __name__ == '__main__':
    main()
    