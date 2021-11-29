def solution(new_id):
    answer = ''
    
    uppers = list(map(chr,range(ord('A'),ord('Z')+1)))
    lowers = list(map(chr,range(ord('a'),ord('z')+1)))
    numbers = list(map(str,range(0,10)))
    print(numbers)
    chars = ['-','_','.']
    for i in range(ord('A'),ord('Z')):
        new_id = new_id.replace(chr(i),chr(i).lower())

    for i in new_id:
        if i in (lowers+numbers+chars):
            answer+=i
    
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if len(answer)==0:
        answer='a'
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    
    while len(answer) <= 2:
        answer += answer[len(answer)-1]

    return answer
    
    
if __name__ == '__main__':
    print(solution(".a."))