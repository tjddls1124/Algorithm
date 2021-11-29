from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    se = set()
    max_order = 0
    comb_list = []
    for order in orders:
        max_order = max(max_order,len(order))
        for c in order:
            se.add(c)
        
    dic = defaultdict(list)
    comb_list = defaultdict(list)
    
    for c in course:
        for order in orders:
            comb_list[c].extend(list(combinations(order,c)))
    
    for c in course:
        if c > max_order:
            continue
        max_c = 0
        for comb in comb_list[c]:
            count = 0
            
            for order in orders:
                for ch in comb:
                    if not ch in order:
                        count-=1
                        break
                count+=1
            if count < 2:
                continue
            if max_c < count:
                dic[c] = [reStr(comb)]
                max_c = count
            elif max_c == count:
                if not reStr(comb) in dic[c]:
                    dic[c].append(reStr(comb))

    for c in course:
        answer.extend(dic[c])
    
    return sorted(answer)

def reStr(comb):
    res = ""
    for c in sorted(comb):
        res+=c
    return res


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
    