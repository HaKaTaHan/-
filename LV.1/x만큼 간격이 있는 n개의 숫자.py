def solution(x, n):
    answer = []

    num = x*n
    if x*n < 0:
        num = num -1
    elif x*n == 0:
        return [0 for i in range(n)]

    else:
        num = num +1

    for i in range(x, num, x):
        answer.append(i)

    return answer


print(solution(0,5))