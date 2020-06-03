#a,b의 대소 관계를 알아야한다.
def solution(a, b):
    answer = 0

    if a<b:
        for i in range(a,b+1):
            answer = answer + i
    else:
        for i in range(b, a+1):
            answer = answer + i
    return answer

print(solution(3,5))