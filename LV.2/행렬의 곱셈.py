def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]

    for i in range(len(arr1)):
        for j, k in enumerate(arr1[i]):
            for m, n in enumerate(arr2[j]):
                answer[i][m] += k * n
            
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
