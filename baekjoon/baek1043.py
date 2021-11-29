'''
거짓말
'''
import sys
N,M = map(int,sys.stdin.readline().split())
liers = list(map(int,sys.stdin.readline().split()))
del liers[0]

from collections import deque
parties = deque()

for _ in range(M):
    party = list(map(int,sys.stdin.readline().split()))
    del party[0]
    parties.append(party)

liers = set(liers)


for _ in range(3000):
    if len(parties) == 0:
        break
    p = parties.popleft()
    isIn = False
    for part in p:
        if part in liers:
            for part in p:
                liers.add(part)
            isIn = True
            break
    if not isIn:
        parties.append(p)


print(len(parties))

    
