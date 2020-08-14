from queue import Queue
def solution(priorities, location):
    answer = 0

    printer = Queue()
    high = max(priorities)

    for i, j in enumerate(priorities):
        v = (i,j)
        printer.put(v)

    while True:
        p = printer.get()
        if p[1] < high:
            printer.put(p)
        else:
            answer = answer + 1
            if p[0] == location:
                break
            priorities.remove(p[1])
            high = max(priorities)
        
    
    return answer

print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([3,3,4,2], 3))

