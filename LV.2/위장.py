from itertools import combinations

def mul(arr):
    res = 1

    for i in arr:
        res *= i

    return res

def solution(clothes):
    answer = 0

    dictClothes = {}

    for i in clothes:
        temp = dictClothes.get(i[1], [])
        temp.append(i[0])
        dictClothes[i[1]] = temp

    temp = []
    for i in dictClothes.keys():
        v = len(dictClothes.get(i))
        temp.append(v+1)
    answer += mul(temp) - 1

    #완전탐색 시간 초과

    # for i in range(1, len(dictClothes.keys())+1):
    #     v = list(combinations(dictClothes.keys(), i))
    #     for j in v:
    #         temp = []
    #         for k in j:
    #             temp.append(len(dictClothes.get(k)))
    #         answer += mul(temp)
        

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))