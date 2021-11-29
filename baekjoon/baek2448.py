'''
백준 2448번
별찍기 11
'''

def single():
    res = ""
    sp = " "
    star = "*"
    res = []
    res.append(sp*2 + star + sp*2)
    res.append(sp*1 + star + sp + star + sp)
    res.append(star*5)
    
    return res
def star_concat(pattern,prevSpace=0):
    res = []
    if prevSpace!=0:
        for p in pattern:
            res.append(prevSpace*" "+p+prevSpace*" ")
    
        return res
    
    for i,p in enumerate(pattern):
        res.append(p+ " "*1+ p)
    return res

def pattern(n):
    if n==3:
        return single()
    prev_pat = pattern(n//2)
    res = []
    
    res.append( star_concat(prev_pat, prevSpace=n//2))
    res.append(star_concat(prev_pat))
    
    return sum(res,[])
    
n = int(input())
for i in pattern(n):
    print(i)