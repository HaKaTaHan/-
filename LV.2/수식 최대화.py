from itertools import permutations
def solution(expression):
    answer = []
    arr = []
    special = set()
    idx = 0

    for i, j in enumerate(expression):
        if not j.isdigit():
            arr.append(int(expression[idx:i]))
            arr.append(j)
            special.add(j)
            idx = i+1
    else:
        if len(expression[idx:]) > 0:
            arr.append(int(expression[idx:]))

    special = list(permutations(special, len(special)))

    for i in special:
        temp = arr[:]
        for j in i:
            count = temp.count(j)
            for m in range(count):
                index = temp.index(j)
                left = temp[index-1]
                right = temp[index+1]

                for k in range(3):
                    temp.pop(index-1)
                
                if j == '-':
                    temp.insert(index-1, left - right)
                elif j == '+':
                    temp.insert(index-1, left + right)
                elif j == '*':
                    temp.insert(index-1, left * right)
        answer.append(abs(temp[0]))
        
    return max(answer)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
