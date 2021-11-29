'''
백준 1541번
잃어버린 괄호
'''
def solution():
    inp_str = input()
    arr = []
    for spt in inp_str.split("-"):
        try:
            arr.append(eval(spt))
        except:
            s = 0
            for v in spt.split("+"):
                s+= int(v)
            arr.append(s)
    print(-1*sum(arr) + arr[0] * 2)
solution()