def solution(n):
    answer = ""
    while True:
        if n == 0:
            break

        if n % 3 == 0:
            answer = '4' + answer
            n = (n//3)-1
        else:
            answer = str(n%3) + answer
            n = n//3

    
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
