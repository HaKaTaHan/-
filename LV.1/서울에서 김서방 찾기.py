import string

def solution(seoul):
    template = '김서방은 ${var}에 있다'
    answer = string.Template(template)

    answer = answer.substitute(var=str(seoul.index("Kim")))
    
    return answer

print(solution(["Jane", "Kim"]))