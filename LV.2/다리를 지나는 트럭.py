def solution(bridge_length, weight, truck_weights):
    answer = 0

    times = [0 for i in truck_weights]
    ing = []

    while True:
        if len(truck_weights) == 0 and len(ing) == 0:
            break

        for i in range(len(ing)):
            if times[0] == bridge_length:
                ing.pop(0)
                times.pop(0)
 
        if len(truck_weights) != 0 and sum(ing) + truck_weights[0] <= weight:
            ing.append(truck_weights[0])
            truck_weights.pop(0)

        for i in range(len(ing)):
            times[i] = times[i]+1

        answer = answer + 1

    return answer


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

