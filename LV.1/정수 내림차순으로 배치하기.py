def solution(n):

    return int(''.join(list(map(str, sorted(str(n))))[::-1]))

print(solution(118372))