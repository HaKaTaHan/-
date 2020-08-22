from math import ceil
def solution(n, words):
    answer = []
    keys = {}

    for i, j in enumerate(words):
        if i == 0:
            keys[j] = j
            continue
        
        if j[0] != words[i-1][-1]:
            p = (i%n)+1
            g = ceil((i+1)/n)
            answer = [p, int(g)]
            break


        if keys.get(j):
            p = (i%n)+1
            g = ceil((i+1)/n)
            answer = [p, int(g)]
            break
        
        keys[j] = j

    if len(answer) == 0:
        answer = [0, 0]

    return answer

"""
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
"""

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
 "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution(2, ['qwe', 'eqwe', 'eqwe']))