import queue

def solution(s):
    answer = ''
    temp = []
    myQueue = queue.PriorityQueue()

    for i in s:
        myQueue.put((ord(i), i))

    for i in range(myQueue.qsize()):
        temp.append(myQueue.get()[1])

    answer = ''.join(temp[::-1])

    return answer

print(solution("Zbcdefg"))