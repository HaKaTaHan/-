from collections import Counter
def balence(p):
    c = Counter(p)

    if c["("] == c[")"]:
        return True
    else:
        return False

def right(p):
    arr = []

    for i, j in enumerate(p):
        if i == 0:
            arr.append(j)
            continue
        
        if len(arr) != 0:
            m = arr.pop()

            if m == "(" and j ==")":
                pass
            else:
                arr.append(m)
                arr.append(j)
        else:
            arr.append(j)

    return len(arr) == 0

def solution(p):
    answer = ''

    u = ""
    b = ""
    
    if len(p) == 0:
        return ""

    if right(p):
        return p

    for i in range(2,len(p)+1,2):
        if balence(p[:i]):
            u = p[:i]
            v = p[i:]
            break
    
    if right(u):
        answer += u + solution(v)
    else:
        answer += "(" + solution(v) + ")"
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))