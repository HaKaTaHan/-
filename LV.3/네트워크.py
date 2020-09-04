def solution(n, computers):
    answer = 0
    visited, need_visit = [], []
    dictComputers = {}
    
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                temp.append(j)
        dictComputers[i] = temp
    
    keys = list(dictComputers.keys())
    need_visit.append(keys.pop(0))
    
    while dictComputers:
        while need_visit:
            temp = need_visit.pop(0)
            if temp not in visited:
                visited.append(temp)
                need_visit += dictComputers.get(temp)
                del dictComputers[temp]
                
        answer += 1
        if len(dictComputers) > 0:
            visited = []
            need_visit = []
            keys = list(dictComputers.keys())
            need_visit.append(keys.pop(0))
            
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]] ))