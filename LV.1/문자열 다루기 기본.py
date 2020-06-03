def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if ord(i) in range(ord('0'), ord('9')+1):
                answer = True
            else:
                answer = False
                break


    return answer

print(solution("0239"))