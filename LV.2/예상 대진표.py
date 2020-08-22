def solution(n,a,b):
    answer = 1
    a = a-1
    b = b-1

    for i in range(n//2):
        if a//2 == b//2:
            break
        else:
            a = a//2
            b = b//2
        answer += 1
    
    return answer

print(solution(8,4,7))