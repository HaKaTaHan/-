import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
   
    while scoville:
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                break 
        s1 = heapq.heappop(scoville)

        if s1 > K:
            break
        s2 = heapq.heappop(scoville)

        heapq.heappush(scoville, s1 + (s2 * 2))

        answer = answer + 1
    

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))