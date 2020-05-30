from collections import Counter
def solution(people, limit):
    answer = 0
    dict_people = Counter(people)
    list_weight = list(dict_people.keys())
    
    list_weight.sort()

    for i in list_weight[::-1]:
        for j in list_weight[::-1]:
            # print(i,j, limit)
            if dict_people[i] == 0:
                break

            if i + j > limit:
                continue
            elif dict_people[j] != 0:
                # print('in')
                bigv, smallv = dict_people[i], dict_people[j]
                if smallv - bigv > 0:
                    # print('smallv > bigv')
                    answer = answer + bigv
                    dict_people[j] = smallv - bigv
                    dict_people[i] = 0
                elif smallv - bigv == 0:
                    # print('smallv == bigv')
                    if i == j:
                        # print('같다',i,j)
                        if bigv == 1:
                            continue
                        else:
                            answer = answer + (bigv // 2)
                        dict_people[i] = bigv - (bigv // 2) * 2
                        # dict_people[j] = 0
                    else:
                        # print('다르다',i,j)
                        answer = answer + bigv
                        dict_people[i] = 0
                        dict_people[j] = 0
                else:
                    # print('smallv < bigv')
                    answer = answer + smallv
                    dict_people[i] = abs(smallv - bigv)
                    dict_people[j] = 0
            # print(dict_people, answer)
        

    for k in dict_people.values():
        answer = answer + k

    return answer

print(solution([40,40,40,40,40,40,40,40,40,40, 80, 50,50,50,50,90,90,80, 80,140], 180))

# 40,40,40,40,40,40,40,40,40,40, 80, 50,50,50,50,90,90,80, 80,140