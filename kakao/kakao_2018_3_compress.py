'''
카카오 2018 blind 3차
압축
'''

def solution(msg):
    answer = []
    di = {}
    index = 0 
    for i in range(ord('A'),ord('Z')+1):
        index += 1
        di[str(chr(i))] = index
    
    i = 0
    st = ''
    ptr = 0 
    res = []
    while True:
        for j in range(1,len(msg)+1):
            if di.get(msg[i:i+j]) != None:
                st = di.get(msg[i:i+j])
                ptr = i+j
                if ptr == len(msg):
                    res.append(st)
                    return res
            else:
                index+=1
                di[msg[i:i+j]] =  index
                i = i+j - 1
                res.append(st)
                break
            

print(solution('A'))