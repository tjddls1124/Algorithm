
b2 = input()
b3 = input()

set2 = set()
set3 = set()


def replace(i:int,s:str,c):
    li = list(s)
    li[i] = c
    return "".join(li)

for i in range(len(b2)):
    set2.add(replace(i,b2,'0'))
    set2.add(replace(i,b2,'1'))

for i in range(len(b3)):
    set3.add(replace(i,b3,'0'))
    set3.add(replace(i,b3,'1'))
    set3.add(replace(i,b3,'2'))
    
print(set2,set3)
set2.remove(b2)
set3.remove(b3)
arr2 = []
for s in set2:
    arr2.append(int(s,base=2))

arr3 = []
for s in set3:
    arr3.append(int(s,base=3))
    
for v in arr2:
    if v in arr3:
        print(v)
