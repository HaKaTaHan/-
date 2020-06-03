import math
def solution(n):
    answer = 0

    if n == 2:
        return 1
    elif n == 3:
        return 2

    for i in range(4, n+1):
        if i % 2 == 0 or i % 3 == 0:
            continue
        if prime(i):
            answer = answer + 1

    return answer + 2

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

print(solution(5))