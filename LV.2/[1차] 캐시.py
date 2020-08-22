def solution(cacheSize, cities):
    answer = 0

    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        i = i.lower()
        
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                cache.pop(0)
                cache.append(i)
            answer += 5

    return answer

"""
LRU에 따라 최근에 hit된 것을 cache 리스트의 가장 마지막 값으로 한다.
"""

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
