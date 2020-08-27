def solution(n):
    answer = 0

    for i in range(1, n+1):
        res = i
        for j in range(i+1, n+1-i):
            res+=j
            if res > n:
                break

            if res == n:
                answer += 1
                break
            
    return answer + 1

print(solution(15))
print(solution(10000))