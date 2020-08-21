from math import gcd
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    
    while len(arr) != 1:
        s1 = arr.pop(0)
        s2 = arr.pop(0)

        v = s1 * s2 // gcd(s1, s2)

        arr.insert(0, v)

    return arr[0]

print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([2,3,6,12]))
print(solution([4,4,4]))
print(solution([2,3,4]))
print(solution([14,2,7]))