def solution(s):
    answer = ''

    idx = 0

    for i in s:
        if i == ' ':
            idx = 0
            answer = answer + i
            continue

        if idx % 2 == 0:
            answer = answer + i.upper()
        else:
            answer = answer + i.lower()

        idx = idx + 1

    return answer

print(solution("try hello world"))