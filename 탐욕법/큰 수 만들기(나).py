def solution(number, k):
    answer = ''

    answercount = len(number) - k
    count = len(number) - k
    length = len(number) - count + 1

    while True:
        head = number[:length]

        king = max(head)

        answer = answer + number[number.find(king)]

        number = number[number.find(king) + 1:]

        count = count - 1

        length = len(number) - count + 1

        if len(answer) == answercount:
            break
        elif len(answer + number) == answercount:
            answer = answer + number
            break
    
    return answer

print(solution('15846287', 5))
