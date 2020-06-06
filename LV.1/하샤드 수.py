def solution(x):
    answer = True

    h = sum(list(map(int, str(x))))

    if x % h == 0:
        answer = True
    else:
        answer = False

    return answer

print(solution(12))