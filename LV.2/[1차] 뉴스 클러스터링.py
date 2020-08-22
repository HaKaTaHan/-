from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = []
    set2 = []

    for i in range(0, len(str1)-1):
        temp = str1[i] + str1[i+1]
        if temp.isalpha():
            set1.append(temp)

    for i in range(0, len(str2)-1):
        temp = str2[i] + str2[i+1]
        if temp.isalpha():
            set2.append(temp)

    n1 = Counter(set1)
    n2 = Counter(set2)

    if len(set1) == 0 and len(set2) == 0:
        answer = 1 * 65536
    else:
        answer = int((sum((n1 & n2).values())/sum((n1 | n2).values()))*65536)
    return answer

print(solution("FRANCE", "french"))
print(solution("aa1+aa2", "AAAA12"))