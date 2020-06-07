import collections
import operator
def solution(N, stages):
    answer = []

    counter = collections.Counter(stages)

    fail = {}


    for i in range(1, N+1):
        if counter[i] == 0:
            fail[i] = 0
        else:
            fail[i] = counter[i] / sum(counter.values())
        del counter[i]
    
    for i in sorted(fail.items(), key=operator.itemgetter(1), reverse=True):
        answer.append(i[0])
        
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))