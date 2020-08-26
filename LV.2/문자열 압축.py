def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)+1):
        count = 1
        temp = ""
        convert = ""
        for j in range(0, len(s), i):
            temp = s[j:j+i]
            if temp == s[j+i:j+i+i]:
                count += 1
            else:
                if count == 1:
                    convert += temp
                else:
                    convert += str(count)+temp

                temp = ""
                count = 1
        if answer > len(convert):
            answer = len(convert)



    return answer

print(solution("aabbaccc"))