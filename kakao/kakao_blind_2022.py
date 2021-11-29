from collections import defaultdict
def solution1(id_list, report, k):
    answer = []
    rep_dic = defaultdict(set)
    user_dic = defaultdict(set)
    
    for r in report:
        spt = r.split()
        rep_dic[spt[1]].add(spt[0])
        user_dic[spt[0]].add(spt[1])
    
    for id in id_list:
        s = 0
        for t in list(user_dic[id]):
            if len(rep_dic[t]) >= k:
                s+=1
        answer.append(s)
            
    
    return answer    


def solution2(n, k):
    answer = 0
    based = base_n(n,k)
        
    for b in based.split('0'):
        if len(b)==0:
            continue
        if isPrime(int(b)):
            answer+=1
    return answer

def base_n(n,b):
    res = []
    ans = ""
    while(n>=b):
        res.append(n % b)
        n = n//b
    res.append(n)
    for i in reversed(res):
        ans+=str(i)
    return ans

def isPrime(n):
    if int(n) <= 1:
        return False 
    i = 2
    while i*i <= n :
        if (n % i) == 0:
            return False
        i+=1
    return True

from collections import defaultdict
from math import ceil
def solution3(fees, records):
    answer = []
    dic = defaultdict(list)
    min_time = fees[0]
    min_fare = fees[1]
    unit_time = fees[2]
    unit_fare = fees[3]
    
    def getFare(time):
        res = min_fare
        if min_time < time:
            res += ceil((time-min_time) / unit_time) * unit_fare
        return res
    
    for record in records:
        r =  record.split()
        dic[r[1]].append(r[0])
    
    
    for k in sorted(dic.keys()):
        l = len(dic[k])
        acc = 0
        i = 0
        while i < l:
            in_time = getTime(dic[k][i])
            out = 0
            if i+1 >= l:
                out = 24 * 60 -1
            else:
                out = getTime(dic[k][i+1])
            i+=2
            acc+=out-in_time
        answer.append(getFare(acc))
            
    return answer
    
    
    
def getTime(t):
    spt = t.split(":")
    return int(spt[0]) * 60 + int(spt[1])



from copy import deepcopy
from collections import defaultdict

def solution4(n, info):
    max_acc = 0
    answer = defaultdict(list)
    def dfs(i,n,acc,res):
        nonlocal max_acc, answer
        point= 0
        if i == len(info):
            if max_acc <= acc:
                max_acc = acc
                answer[acc].append(tuple(res))
            return
        ran = range(n+1)
        if i==len(info)-1:
            ran = [n]
        for j in ran:
            if info[i] == 0 and j == 0:
                point = 0
            elif j > info[i]:
                point = 10-i
            else:
                point = -(10-i)
            res.append(j)
            dfs(i+1,n-j,acc+point,res)
            res.pop()
    dfs(0,n,0,[])
    
    
    if max_acc==0:
        return [-1]
    
    ans = answer[max_acc][0]
    if len(answer[max_acc]) > 1:
        ans = sorted(answer[max_acc],key= lambda x:x[::-1], reverse=True)[0]
    
    
    return list(ans)

from collections import deque
def solution5(info, edges):
    
    def getConnected(n):
        res = []
        for e in edges:
            if n == e[0]:
                res.append(e[1])
        return res
    answer = 0
    q = list()
    q.append(0)
    
    max_sheep= 1
    visited = [False] * len(info)
    
    def dfs(q,p,kind):
        q.remove(p)
        nonlocal max_sheep
        
        sheep=kind[0]
        wolf = kind[1]
        if info[p]==0:
            sheep+=1
        else:
            wolf+=1
        
        if sheep <= wolf:
            return
        
        for n in getConnected(p):
            q.append(n)
        
        max_sheep = max(max_sheep,sheep)
        
        new_q = deepcopy(q)
        for node in q:
            q = deepcopy(new_q)
            dfs(q,node,(sheep,wolf))
            
    dfs(q,0,(0,0))
    
    return max_sheep    

ST = 0
END = 1
LASTEND = 2
def solution(board, skill):
    answer = 0
    maps = deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            maps[i][j] = []

    vals = [0] * len(board)
    for i in range(len(skill)):
        sk = skill[i]
        x1 = sk[1]
        y1 = sk[2]
        x2 = sk[3]
        y2 = sk[4]
        
        if sk[0] == 1:
            vals[i] = -sk[5]
        else:
            vals[i] = sk[5]
        
        maps[x1][y1].append((i,ST))
        if y2+1 < len(board[0]):
            maps[x1][y2+1].append((i,END))
            maps[x2][y2+1].append((i,LASTEND))

    print(maps)
    
    
    val = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(maps[i][j])==0:
                maps[i-1][j]
            for si in maps[i][j]:
                sk_num, signal = si
                if signal == ST:
                    val += vals[sk_num]
                if signal == END:
                    val -= vals[sk_num]
                board[i][j] += val
                
            if board[i][j] >= 1:
                answer+=1
    
    return answer



    

if __name__ == '__main__':
    
    #a = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	)
    #print(a)
    
    b = solution5(info = [0,0,1,1,1,0,1,0,1,0,1,1], edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
    print(b)