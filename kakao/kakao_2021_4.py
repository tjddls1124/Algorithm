def solution(n, s, a, b, fares):
    INF = 10**2
    answer = INF
    maps = [[INF]*(n+1) for _ in range(n+1)]
    
    for f in fares:
        a1,b1,c1 = f
        maps[a1][b1] = c1
        maps[b1][a1] = c1
    for i in range(n+1):
        maps[i][i] = 0
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                maps[j][k] = min(maps[j][k],maps[j][i] + maps[i][k])        
    for t in range(1,n+1):
        if answer > maps[s][t] + maps[t][a] + maps[t][b]:
            answer = maps[s][t] + maps[t][a] + maps[t][b]
    
    return answer


if __name__ == '__main__':
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    