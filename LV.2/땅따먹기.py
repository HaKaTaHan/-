def solution(land):
    answer = 0
    big = max(land[0])
    idx = land[0].index(big)
    for i, j in enumerate(land[1:]):
        for k in range(len(j)):
            if k != idx:
                land[i+1][k] += big
            else:
                temp = max(land[i][:idx] + land[i][idx+1:])
                land[i+1][k] += temp
        big = max(land[i+1])
        idx = land[i+1].index(big)

    answer = max(land[-1])

    return answer

"""
def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1], land[i][2], land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], land[i][2], land[i][3]) + land[i+1][1]
        land[i+1][2] = max(land[i][0], land[i][1], land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0], land[i][1], land[i][2]) + land[i+1][3]
        answer = max(land[i+1])
    return answer

"""
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))