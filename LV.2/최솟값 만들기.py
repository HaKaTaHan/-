def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    for i in range(len(A)-1):
        lmin, rmax = A[0], B[-1]
        lmax, rmin = A[-1], B[0]

        if lmin * rmax < lmax * rmin:
            answer += lmin * rmax
            A.pop(0)
            B.pop(-1)
        else:
            answer += lmax * rmin
            A.pop(-1)
            B.pop(0)

    return answer + A[0] * B[0]

"""
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
"""

print(solution([1,4,2], [5,4,4]))
print(solution([1,2],[3,4]))