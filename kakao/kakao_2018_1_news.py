'''
카카오 2018 blind 1차
뉴스 클러스터링
'''
    

def solution(str1, str2):
      
    return int(zacard(castString(str1),castString(str2)) * 65536)

def castString(str1):
    li = []
    for i in range(len(str1)-1):
        unit = str1[i] + str1[i+1]
        if(unit.isalpha()):
            li.append(unit.lower())
            
    print(li)
    return li

def zacard(A,B):
    uni = set(A).union( set(B) )
    inter = set(A).intersection(set(B))
    len_uni = 0 
    for i in uni:
        len_uni += max(A.count(i),B.count(i))
    
    
    len_inter = len(inter)
    if(len_uni==0):
        return 1
    for i in inter:
        len_inter += min(A.count(i), B.count(i)) - 1
    print(len_inter, len_uni)
    
    return len_inter/ len_uni


if __name__ == '__main__':
    print(zacard(["1", "2", "4", "4", "4"],["4", "4", "5", "6", "7", "8", "8"]))
    