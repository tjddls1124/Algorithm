'''
백준 15650번
N과 M 2

'''
from itertools import combinations

N, M = map(int, input().split())
li = []
for i in range(1,N+1):
    li.append(i)
    
for l in list(combinations(li, M)):
    for i in l:
        print(i,end=' ')
    print()