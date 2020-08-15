def solution(progresses, speeds):
    answer = []

    while len(progresses) * -1 != sum(progresses):
        # 하루 진행
        for i in range(len(progresses)):
            if progresses[i] != -1:
                progresses[i] = progresses[i] + speeds[i]
                if progresses[i] > 100:
                    progresses[i] = 100


        temp = 0
        for i, j in enumerate(progresses):
            print(progresses)
            print(i)

            if j == 100:
                temp = temp + 1
                progresses[i] = -1
                speeds[i] = -1
            elif j == -1:
                pass
            else:
                break
        print()

        if temp != 0:
            answer.append(temp)

        
        # temp = 0
        # if progresses[0] == 100:
        #     temp = temp + 1
        #     progresses.pop(0)
        #     speeds.pop(0)

        #     for i in progresses:
        #         if i == 100:
        #             temp = temp + 1
        #             progresses.pop(0)
        #             speeds.pop(0)
        #         else:
        #             break

        # if temp != 0:
        #     answer.append(temp)


    return answer

print(solution([93,30,55],[1,30,5]))