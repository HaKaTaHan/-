def solution(n):
    ans = 0

    while n != 0:
        if n % 2 != 0:
            ans += 1
        n = n // 2

    return ans

"""
def solution(n):
    return bin(n).count('1')
"""

print(solution(5))
print(solution(6))
print(solution(5000))