def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr1[0]))] for row in range(len(arr1))]

    for i, j in enumerate(arr1):
        for p, q in enumerate(j):
            answer[i][p] = q + arr2[i][p]

    return answer


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))