def solution(citations):
    answer = 0

    citations.sort()
    papers = len(citations)
    
    while True:
        c = 0
        for i in citations:
            if i >= answer:
                c = c + 1
        
        if c >= answer and papers-c <= answer:
            answer = answer + 1
        else:
            answer = answer - 1
            break
            
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([31,66]))
print(solution([3,3,3,3]))