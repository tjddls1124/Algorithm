'''
N과 M 12
'''

N,M = map(int,input().split())
arr = set(map(int,input().split()))


arr = sorted(list(arr))
res = []

def rec(index,depth):
    if depth==M:
        for v in res:
            print(v,end=' ')
        print()
        return
    for i in range(index, len(arr)):
        res.append(arr[i])
        rec(i, depth+1)
        res.pop()
rec(0,0)