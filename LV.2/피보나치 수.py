def solution(n):
    m = 1234567
    A = [0, 1]

    for i in range(2, n+1):
        A.append(A[i-1] + A[i-2])

    return A[n] % m

print(solution(3))
print(solution(5))