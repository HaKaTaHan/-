from itertools import combinations
from collections import Counter
def solution(relation):
    answer = []
    cols = [x for x in range(len(relation[0]))]
    keys = []

    for i in range(1, len(cols)+1):
        temp = combinations(cols, i)
        
        for j in temp:
            keys.append(j)

    for i in keys:
        arr = ["" for x in range(len(relation))]

        for j in i:
            for k in range(len(relation)):
                arr[k] += relation[k][j]
        
        temp = Counter(arr)

        if len(temp) == len(relation):
            i = set(i)

            if len(answer) == 0:
                answer.append(i)
            else:
                for m in answer:
                    if m & i == m:
                        break
                else:
                    answer.append(i)
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([["b","2","a","a","b"],["b","2","7","1","b"],["1","0","a","a","8"],["7","5","a","a","9"],["3","0","a","f","9"]]))
