def solution(d, budget):
    answer = 0

    if sum(d) == budget:
        return len(d)

    d.sort()
    price = 0
    for i in d:
        
        price = price + i
        if price > budget:
            break

        answer = answer + 1

    return answer


print(solution([2,2,3,3], 10))
print(solution([1,3,2,5,4], 9))