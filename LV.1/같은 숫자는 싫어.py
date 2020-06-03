def solution(arr):
    answer = []

    answer.append(arr[0])
    arr.pop(0)

    idx = 0

    for i in arr:

        if i == answer[idx]:
            continue
        else:
            print(i)
            answer.append(i)
            idx = idx + 1
    
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))