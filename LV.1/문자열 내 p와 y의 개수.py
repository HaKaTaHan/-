def solution(s):
    answer = True

    s = s.lower()

    p = s.count('p')
    y = s.count('y')

    if p == y:
        answer = True
    elif p == 0 and y == 0:
        answer = True
    elif p != y:
        answer = False

    return answer

print(solution("pPoooyY"))