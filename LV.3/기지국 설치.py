from math import ceil

def solution(n, stations, w):
    answer = 0
    cover = w*2+1
    notCoverArr = []
    beforeMaxCover = 0
    
    for i in range(len(stations)):
        leftCover = stations[i] - w - 1
        if i == 0:
            beforeMaxCover = stations[i] + w
            notCoverArr.append(ceil((leftCover)/cover))
            continue

        notCoverArr.append(ceil((leftCover - beforeMaxCover)/cover))
        beforeMaxCover = stations[i] + w
    
    if beforeMaxCover < n:
        notCoverArr.append(ceil((n - beforeMaxCover)/cover))
    
    answer = sum(notCoverArr)
    return answer