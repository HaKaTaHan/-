def solution(n):
    answer = 0

    bn = list(bin(n))
    
    while True:
        n += 1
        bx = list(bin(n))

        if bn.count('1') == bx.count('1'):
            answer = n
            break
    
    return answer

print(solution(78))
print(solution(15))