import math
def solution(n, m):
    k = math.gcd(n, m)
    b = (n // k) * (m //k) * k

    return [k, b]

print(solution(3,12))