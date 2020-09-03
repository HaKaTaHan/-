from math import ceil

def solution(n, stations, w):
    answer = 0
    cover = w*2+1
    beforeMaxCover = 0
    
    for i in range(len(stations)):
        leftCover = stations[i] - w - 1
        if i == 0:
            beforeMaxCover = stations[i] + w
            answer += ceil((leftCover)/cover)
            continue
        
        answer += ceil((leftCover - beforeMaxCover)/cover)
        beforeMaxCover = stations[i] + w
    if beforeMaxCover < n:
        answer += ceil((n - beforeMaxCover)/cover)
    return answer