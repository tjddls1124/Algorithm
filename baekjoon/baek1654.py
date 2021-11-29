


'''
백준 1654 랜선자르기
'''
#binary search
res = 0

def bs(low, high,lines, N ):
    global res,tmp_mid
    mid = int((low + high) / 2)
    tmp  = 0
    if low > high:
        return
    
    for line in lines:
        tmp += int(line/mid)
    if tmp >= N :
        if res == mid:
            return
        res = mid
        bs(mid+1,high,lines,N)   
    else:
        bs(low,mid-1,lines,N)

def main():
    try:
        K, N = input().split()
        K = int(K)
        N = int(N)
        lines = []
        for i in range(K):
            lines.append(int(input()))
        if max(lines)==1:
            print(1)
            return
        
        bs(0,max(lines),lines,N)
        print(res)
    except:
        print(1)

if __name__ == '__main__':
    main()
    

