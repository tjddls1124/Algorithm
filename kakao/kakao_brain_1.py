
'''
Kakao 브레인 하계인턴십
해커랭크 4문제

'''
def areAlmostEquivalent(s, t):
    # Write your code here
    res = []
    for i in range(len(s)):
        res.append(isDiffer(s[i],t[i]))
        
    return res
    
def isDiffer(s,t):
    se = set()
    for c in s:
        se.add(c)
    for c in t:
        se.add(c)
        
    for c in se:
        if abs(t.count(c)-s.count(c)) > 3 :
           return "NO"
    return "YES" 
    
    
def minTime(processorTime, taskTime):
    processorTime = sorted(processorTime,key=lambda x: -x)
    taskTime = sorted(taskTime)
    li = []
    
    p_i =0
    p_time = []
    for i, task in enumerate(taskTime):
        if i!=0 and i%4==0:
            p_i+=1
        li.append(task+processorTime[p_i])
        
    
    return max(li)
    



def fountainActivation(locations):
    #dp
    dp = [0]
    for i,loc in enumerate(locations):
        dp.append(i+1)
    
    n = len(locations)
    for i,loc in enumerate(locations):
        pos = i+1
        maxRange = min(pos+ locations[i], n)
        minRange = max(1,pos-locations[i])
        
        print(minRange, maxRange)
        for j in range(minRange,maxRange+1):
            dp[j] = min(dp[j], dp[minRange-1]+1)
            
    
            
    print(dp)    
    
    return dp[n]

'''
timecomplexity -> Java 로 풀어 해결
'''
def encryptionValidity(instructionCount, validityPeriod, keys):
    checks = instructionCount * validityPeriod
    res = []
    max_div = 0
    
    valid = [0 for i in range(pow(10,5))]
    
    keys = sorted(keys, key=lambda x:-x)

    for key in keys:
        count = 0 
        for t in keys:
            if key % t == 0 :
                 
                count+=1
        max_div = max(max_div,count)
    
    
    
    stren = pow(10,5) * max_div
    if checks > stren:
        res.append(1)
    else:
        res.append(0)
        
    res.append(stren)
    
    return res
    


if __name__ == '__main__':
    print(encryptionValidity(100,1000,[2,4]))