def solution(n):
    answer = 0

    base = 100000000

    while True:
        if base == 0:
            break
        temp = n // base

        if temp != 0:
            answer = answer + temp
            n = n - temp * base
            base = base // 10
        else:
            base = base // 10
            continue


    return answer

print(solution(987))