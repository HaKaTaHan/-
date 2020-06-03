#우선순위 큐 생각남
import queue
def solution(strings, n):
    answer = []
    myQueue = queue.PriorityQueue()

    for i in strings:
        myQueue.put((ord(i[n]), i))

    for i in range(myQueue.qsize()):
        answer.append(myQueue.get()[1])

    return answer

print(solution(['abce', 'abcd', 'cdx'], 1))