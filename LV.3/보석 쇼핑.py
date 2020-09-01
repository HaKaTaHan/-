def solution(gems):
    keys = []
    jewels = len(set(gems))
    dictPerfect = {}
    l = 100000

    for idx, gem in enumerate(gems):
        if dictPerfect.get(gem) == None:
            dictPerfect[gem] = idx + 1
        else:
            del dictPerfect[gem]
            dictPerfect[gem] = idx + 1
        
        if len(dictPerfect) == jewels:
            start = 0
            for i in dictPerfect:
                start = dictPerfect.get(i)
                break
            
            end = dictPerfect.get(gem)
            if end - start < l:
                l = end - start
                keys = [start, end]
                
    return keys