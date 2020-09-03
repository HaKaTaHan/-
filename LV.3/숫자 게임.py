def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    k=0
    for a in A:
        for i in range(len(B)-k):
            if B[0] > a:
                answer += 1
                B.remove(B[0])
                break
            else:
                temp = B.pop(0)
                B.append(temp)
                k+=1
                
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([1,7,11,12], [1,1,1,3]))

# from collections import Counter
# def solution(A, B):
#     answer = 0
#     A.sort()
#     B = Counter(B)
#     sortB = list(sorted(B.keys()))
#     print(sortB)
#     for a in A:
#         for b in sortB:
#             print(a, b, sortB)
#             if b > a:
#                 if B.get(b) != 0:
#                     answer += 1
#                     B[b] = B.get(b) - 1
#                     break
#                 else:
#                     continue
#             else:
#                 continue
                
#     return answer
