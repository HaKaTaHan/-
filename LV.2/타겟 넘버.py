from itertools import combinations
def solution(numbers, target):
    answer = 0
    
    all =sum(numbers)
    l = len(numbers)

    for i in range(1,len(numbers)+1):
        cl = list(combinations(numbers, i))
        for j in cl:
            if all - sum(j) * 2 == target:
                answer += 1
            
            
    return answer

print(solution([1,1,1,1,1], 3))