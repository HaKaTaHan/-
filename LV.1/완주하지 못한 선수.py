from collections import Counter

def solution(participant, completion):
    answer = ''

    full = Counter(participant)

    goal = Counter(completion)

    for i in full.keys():
        if not i in goal:
            answer = i
        else:
            if full[i] != goal[i]:
                answer = i

    return answer

print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))