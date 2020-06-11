
def solution(dartResult):
    answer = []

    for i in dartResult:
        if i.isdigit():
            if i == '0' and len(answer) !=0 and answer[-1] == 1:
                answer[-1] = 10
            else:
                answer.append(int(i))
        else:
            if i == '*':
                if len(answer) == 1:
                    answer[-1] = answer[-1] * 2
                else:
                    answer[-2] = answer[-2] * 2
                    answer[-1] = answer[-1] * 2
            elif i == '#':
                answer[-1] = answer[-1] * (-1)
            elif i == 'S':
                answer[-1] = answer[-1] ** 1
            elif i == 'D':
                answer[-1] = answer[-1] ** 2
            elif i == 'T':
                answer[-1] = answer[-1] ** 3

            



    return sum(answer)


print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1D2S#10S'))