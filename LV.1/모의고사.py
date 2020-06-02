def solution(answers):
    answer = []

    num1 = [1,2,3,4,5] * 8
    num2 = [2,1,2,3,2,4,2,5] * 5
    num3 = [3,3,1,1,2,2,4,4,5,5] * 4

    alzip = list(zip(num1, num2, num3))

    count = {1:0, 2:0, 3:0}

    for i, j in enumerate(answers):
        i = i % 40

        if j in alzip[i]:
            if j == alzip[i][0]:
                count[1] = count[1] + 1
            if j == alzip[i][1]:
                count[2] = count[2] + 1
            if j == alzip[i][2]:
                count[3] = count[3] + 1

    for i in count.keys():
        if len(answer) == 0:
            answer.append(i)
        elif count[answer[-1]] < count[i]:
            answer.clear()
            answer.append(i)
        elif count[answer[-1]] == count[i]:
            answer.append(i)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]))