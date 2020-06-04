def solution(s, n):
    answer = ''

    a,z,A,Z = ord('a'),ord('z'),ord('A'),ord('Z')

    for i in s:
        if i == ' ':
            answer = answer + i
            continue

        temp = ord(i) + n
        
        if i.isupper() and temp > Z:
            print(temp, Z)
            temp = A + (temp - Z)
        elif i.islower() and temp > z:
            print(temp, z)
            temp = a + (temp - z)

        answer = answer + chr(temp)

    return answer

print(solution("a B z w", 4))