'''
백준 1081번
체스판 다시 칠하기
'''
def rep(c):
    if c==0:
        return 'W'
    else:
        return 'B'
def makeBoard(m,n,isWhite):
    board = []
    for i in range(m):
        tmp = ""
        for j in range(n):
            tmp += rep(((i+j+isWhite)%2))
        board.append(tmp)
    return board

def main():
    board = []
    m,n = input().split()
    m = int(m)
    n = int(n)
    for i in range(m):
        board.append(input())    
    whiteBoard = makeBoard(m,n,0)
    res = []
    wCount = 0
    for row in range(m-7):
        for col in range(n-7):        
            wCount = 0
        
            for i in range(8):
                for j in range(8):
                    if whiteBoard[i][j] != board[i+row][j+col]:
                        wCount +=1            
        
            res.append(min(wCount,64-wCount))
    print(min(res))
if __name__ == '__main__':
    main()
    