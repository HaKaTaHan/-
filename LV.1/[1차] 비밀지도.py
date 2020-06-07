def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:]

        if len(temp) < n:
            temp = ('0'*(n-len(temp)))+temp

        strtemp = ''
        for j in temp:
            if j == "1":
                strtemp = strtemp + '#'
            elif j == "0":
                strtemp = strtemp + ' '

        answer.append(strtemp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))