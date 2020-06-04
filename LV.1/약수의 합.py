import math

def solution(n):
    answer = 0

    setN = set()

    for i in range(1, n+1):
        setN.add(math.gcd(n, i))

    answer = sum(list(setN))

    return answer

print(solution(12))