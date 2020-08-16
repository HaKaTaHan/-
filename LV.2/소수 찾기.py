import itertools
import math

def prime(x):
    
    if x == 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    numArray = set()

    for i in range(1, len(numbers)+1):
        temp = list(itertools.permutations(numbers, i))
        for j in temp:
            numArray.add(int(''.join(j)))

    for i in list(numArray):
        if prime(i):
            answer = answer + 1

    return answer

print(solution("17"))
print()
print(solution("011"))