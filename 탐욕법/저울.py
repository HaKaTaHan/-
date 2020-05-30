def solution(weight):
    answer = 0

    weight.sort()

    for i in weight:
        if answer+1 < i:
            break
        else:
            answer = answer+i

    return answer + 1

print(solution([2,3,4]))

#효율성 문제
# def solution(weight):
#     answer = 0

#     weight.sort()
#     maxValue = sum(weight)
    
#     for i in range(1, maxValue+1):
#         Value = i
#         for j in weight[::-1]:
#             if j > Value:
#                 continue
#             else:
#                 Value = Value - j

#         if Value != 0:
#             answer = i
#             break
        
#         if i == maxValue:
#             answer = maxValue + 1

#     return answer

# print(solution([3,1,6,2,7,30,1,22]))