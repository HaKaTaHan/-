def jinbub(x, base):
    res = []

    if x == 0:
        return str(0)

    while True:
        if x == 0:
            break

        res.append(str(x % base))
        x = x//base
    
    return reversed(res)
def solution(n, t, m, p):
    answer = ''
    arr = []
    p -= 1
    count = 0

    overTen = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    for i in range(t*m):
        arr += jinbub(i, n)

    
    while True:
        if count == t:
            break

        temp = arr[p]

        if overTen.get(temp):
            answer += overTen.get(temp)
        else:
            answer += temp

        p += m
        count += 1
    
    
    return answer

print(solution(2,4,2,1))