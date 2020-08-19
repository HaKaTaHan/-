def solution(s):
    answer = []
    s=s[:-2]
    s= s.replace("{","")
    s= s.split("},")
    mTuple = []

    for i in s:
        mTuple.append(i.split(','))

    for i in range(len(mTuple)):
        head = min(mTuple, key=len)
        for j in head:
            if int(j) not in answer:
                answer.append(int(j))
        mTuple.remove(head)
 
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
