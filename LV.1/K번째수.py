def solution(array, commands):
    answer = []

    for i in commands:
        start, end, pick = i[0]-1, i[1]-1, i[2]-1

        temp = array[start:end+1]

        temp.sort()

        answer.append(temp[pick])
        

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))