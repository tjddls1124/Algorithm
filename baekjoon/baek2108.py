
def absNum(num):
    if num > 4000:
        return num-10000
    else:
        return num
    
import sys
N = int(input())
li = []
for i in range(N):
    read =  int(sys.stdin.readline())
    li.append(read)

print(f'{round(sum(li) / len(li))}')
li = sorted(li)
print(li[len(li)//2])

visited = {}
for i in li:
    if i not in visited.keys():
        visited[i] = 0
    visited[i]+=1
res = []
for k,v in visited.items():
    if v == max(visited.values()):
        res.append(k)
sorted(res)
if len(res)==1:
    print(res[0])
else:
    print(res[1])
    
print(max(li)-min(li))
