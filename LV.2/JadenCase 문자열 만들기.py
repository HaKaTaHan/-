def solution(s):
    answer = []

    s = s.split(" ")
    for i in s:
        answer.append(i.lower().capitalize())
        
    return ' '.join(answer)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("Hello  World"))