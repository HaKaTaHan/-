def solution(s):
    answer = 0

    if s.isdigit():
        answer = int(s)
    else:
        if s[0] == '+':
            answer = int(s[1:])
        elif s[0] == '-':
            answer = -int(s[1:])

    return answer

print(solution("-1234"))