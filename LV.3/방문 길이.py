def solution(dirs):
    answer = 0
    step = {"U": (0,1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    dictRoute = {}
    start = [0, 0]
    
    for i in dirs:
        x, y = start[0], start[1]
        oneStep = step.get(i)
        start[0], start[1] = start[0] + oneStep[0], start[1] + oneStep[1]
        if start[0] > 5 or start[1] > 5 or start[0] < -5 or start[1] < -5:
            start[0], start[1] = start[0] - oneStep[0], start[1] - oneStep[1]
            continue
        else:
            route = str(x) + str(y) + str(start[0]) + str(start[1])
            backRoute = str(start[0]) + str(start[1]) + str(x) + str(y)
            
            dictRoute[route] = 1
            dictRoute[backRoute] = 1
            
    answer = len(dictRoute.keys()) // 2
            
    return answer