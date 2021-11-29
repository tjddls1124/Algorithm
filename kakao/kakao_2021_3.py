from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(lambda: [0]*300)
    
    for i in info:
        q=[""]
        for spt in i.split():
            if not spt.isdigit():
                new_q = []
                for q_str in q:
                    new_q.append(q_str)
                    new_q.append(q_str+spt)
                q = new_q
            else:
                for q_str in q:
                    dic[q_str][int(spt)] += 1
    for k in dic.keys():
        s = 0
        for j in reversed(range(len(dic[k]))):
            s+= dic[k][j]
            dic[k][j] = s
    
    for q in query:
        q_str = ""
        for spt in q.split():
            if spt=='and' or spt=='-':
                continue
            if spt.isdigit():
                answer.append((dic[q_str][int(spt)]))
            else:
                q_str+=spt
    
            
    return answer

if __name__ == '__main__':
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
    