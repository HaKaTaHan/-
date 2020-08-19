def solution(brown, yellow):
    answer = []

    all = brown + yellow
    h = 3

    while True:
        w=int(all/h)
        if w >= h:
            y = (h-2) * (w-2)
            b = all - y
            print(w, h, b, y)
            print()
            if b == brown and y == yellow:
                answer=[w,h]
                break
        h += 1

    return answer


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))