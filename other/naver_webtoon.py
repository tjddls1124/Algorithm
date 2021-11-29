
#solution 3
def solution3(letters, k):
    # two pointer
    
    #zbgaj
    
    #tcdjazb
    
    arr = ['0'] * k
    answer = ''
    i = 0 
    j = i + k
    p = 0
    while p < len(letters):
        added_p = 0
        
        #if p+k > len(letters):
        added_p = len(letters)- p
        print(added_p)
        
        for index,v in enumerate(arr):
            if k - index > added_p:
                continue
            if ord(v) < ord(letters[p]):
                for i in range(index, k):
                    arr[i] = letters[p+i-index]
                p += k - index -1
                break
        p+=1
    print(arr)
    
    
    return answer



def solution(letters, k):
    #사전순이 가장 큰 배열을 저장
    N = len(letters)
    dp = [ [''] * len(letters) for i in range(k+1) ]
    
    for i in range(N):
        dp[0][i] = ""
        
        
    for t in range(1,k+1):
        for i in range(N):
            if i < t-1 :
                continue
            if dp[t-1][i-1] + letters[i] >=  dp[t][i-1]:
                dp[t][i] = dp[t-1][i-1] + letters[i]
            else:
                dp[t][i] = dp[t][i-1]
    print(dp)
    return dp[k][N-1]
    
    
    
    
    
    

#solution 2 
dictionary = []
alps = ['A','E','I','O','U']

import sys
sys.setrecursionlimit(10**4)

def solution2(word):
    answer = 0
    dfs("","",0)
    return dictionary.index(word)
    
def dfs(al, word, depth):
    if depth == 6:
        return
    
    word += al
    dictionary.append(word)
    for w in alps:
        dfs(w,word,depth+1)

# end solution2


#solution 1
from itertools import permutations

def solution_1(S, pattern):
    permutations(pattern)
    
    patterns = set()
    count = 0
    
    arr = list((permutations(pattern, len(pattern))))
    for l in arr:
        s = ""
        for sub in l:
            s+=sub
        patterns.add(s)
    print(patterns)
    for i in range(len(S)):
        j = len(pattern)
        subs = S[i:i+j]
        j+=1
        print(subs)
        if subs in patterns:
            count+=1
    
    
    return count

if __name__ == '__main__':
    a = solution("zbgaj",3)
    print(a)
    
    