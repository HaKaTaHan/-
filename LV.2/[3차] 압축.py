def solution(msg):
    answer = []
    dictionary = {}

    for i in range(ord('A'), ord('Z')+1):
        dictionary[chr(i)] = i - ord('A') + 1

    while True:
        if len(msg) == 0:
            break

        bigiter = reversed(list(dictionary.keys()))
        for i in bigiter:
            if i == msg[:len(i)]:
                value = dictionary.get(i)
                answer.append(value)
                temp = msg[len(i):]

                if len(temp) != 0:
                    dictionary[msg[:len(i)+1]] = len(dictionary) + 1

                msg = temp
                break

    return answer
 
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))