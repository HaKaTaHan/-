def solution(n, lost, reserve):
    answer = n - len(lost)
    temp = []
    for i in lost:
        if i in reserve:
            answer = answer + 1
            temp.append(i)
    
    for k in temp:
        lost.remove(k)
        reserve.remove(k)
            
    for j in reserve:
        if len(lost) == 0:
            break
            
        before = j - 1
        after = j + 1
        
        if before in lost:
            answer = answer + 1
            lost.remove(before)
        elif after in lost:
            answer = answer + 1
            lost.remove(after)
    
    return answer