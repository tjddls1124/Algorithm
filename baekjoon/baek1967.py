'''
백준 1967번
트리의 지름
'''


n = int(input())
import sys

sys.setrecursionlimit(10**6)

from collections import defaultdict
dic = defaultdict(list)

for _ in range(n-1):
    a,b,c = map(int,input().split())
    dic[a].append((b,c))

def recur(node):
    if len(dic[node])==0:
        return 0,0
    
    single = 0
    total = 0
    tmp = []
    for tup in dic[node]:
        single,tmp_to = recur(tup[0])
        total = max(total,tmp_to)
        tmp.append(single + tup[1])
    sort = sorted(tmp,reverse=True)
    res = sort[0]
    if len(sort)>1:
        res = sort[0] + sort[1]
    return sort[0], max(total,res)

print(recur(1)[1])