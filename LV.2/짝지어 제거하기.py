def solution(s):
    answer = 1
    s = list(reversed(s))
    stack = []

    while s:
        if len(s) > 1:
            v1 = s.pop()
            v2 = s.pop()

            if v1 == v2:
                pass
            else:
                s += v2
                if len(stack) != 0:
                    v3 = stack.pop()
                    if v1 == v3:
                        pass
                    else:
                        stack += v3
                        stack += v1
                else:
                    stack += v1
        elif len(s) == 1:
            v1 = s.pop()
            if len(stack) != 0:
                v2 = stack.pop()
                if v1 == v2:
                    pass
                else:
                    stack += v2
                    stack += v1
            else:
                stack += v1

    if len(stack) != 0:
        answer = 0
    return answer

"""
def solution(s):
    t = []
    for i in s:
        if not t:
            t.append(i)
        elif t[-1] == i:
            t.pop()
        else:
            t.append(i)
    return 1 if len(t) == 0 else 0
"""

print(solution("baabaa"))
print(solution("cdcd"))