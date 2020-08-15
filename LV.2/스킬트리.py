def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        temp = ""
        for j in i:
            if j in skill:
                temp = temp + j

        if temp == skill[:len(temp)]:
            answer = answer + 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))