'''
2개 이하로 다른 비트
'''
def solution(numbers):
    answer = []
    for num in numbers:
        bi = bin(num)[2:]
        res = ""
        if bi.count("0") == 0:
            bi = "0" + bi
        bi = bi[::-1]
        i = -1
        s = list(bi)
        print(s)
        while True:
            i+=1
            if bi[i]=='0':
                s[i] = '1'
                break
        while True:
            i-=1
            if i < 0:
                break
            if bi[i]=='1':
                s[i]='0'
                break
        print(s)
        print(int("".join(s),base=2))
                    
        answer.append(res)
        
    return answer

solution([7])