# 우선순위 큐가 생각남
import queue
def solution(arr, divisor):
    answer = []
    myQueue = queue.PriorityQueue()

    for i in arr:
        if i % divisor == 0:
            myQueue.put(i)

    if myQueue.qsize() == 0:
        answer.append(-1)
    else:
        for i in range(myQueue.qsize()):
            answer.append(myQueue.get())

    

    return answer

print(solution([5, 9, 7, 10], 5))