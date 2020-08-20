def solution(s):
    answer = True
    
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue

        temp = stack.pop()

        if temp + i != "()":
            stack.append(temp)
            stack.append(i)

    if len(stack) != 0:
        answer = False
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))