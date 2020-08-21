from itertools import combinations
from math import sqrt
def prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False

    return True

def solution(nums):
    answer = 0

    c = list(combinations(nums, 3))

    for i in c:
        if prime(sum(i)):
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))