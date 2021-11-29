'''
구간 합 구하기
'''
import sys
N, M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

acc = [0]
s = 0
for t in arr:
    s+=t
    acc.append(s)
res = []
for _ in range(M):
    st, end = map(int,sys.stdin.readline().split())
    res.append(acc[end] - acc[st] + arr[st-1])
    
for v in res:
    print(v)