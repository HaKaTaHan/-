"""
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
"""
#바닥 위
#     if y == 0:
#         keys[str(x)+str(y)+str(0)] = True
#         return True

#     #보의 한쪽 끝 부분 위
#     if keys[str(x)+str(y)+str(1)] or keys[str(x-1)+str(y)+str(1)]:
#         keys[str(x)+str(y)+str(0)] = True
#         return True

#     #다른 기둥 위
#     if keys[str(x)+str(y-1)+str(0)]:
#         keys[str(x)+str(y)+str(0)] = True
#         return True

# 한 쪽 끝부분 기둥 위
#     if keys[str(x)+str(y-1)+str(0)] or keys[str(x+1)+str(y-1)+str(0)]:
#         keys[str(x)+str(y)+str(1)] = True
#         return True

#     # 양 쪽 끝부분이 다른 보와 동시에 연결
#     if keys[str(x-1)+str(y)+str(1)] and keys[str(x+1)+str(y)+str(1)]:
#         keys[str(x)+str(y)+str(1)] = True
#         return True
def check(answer):
    res = True
    
    for x, y, _type in answer:
        if _type == 0:
            if y == 0 or [x,y-1,0] in answer or ([x,y,1] in answer or [x-1, y,1] in answer):
                pass
            else:
                return False
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                pass
            else:
                return False

    return res

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        if frame[3] == 1:
            answer.append([frame[0], frame[1], frame[2]])
            if check(answer) == False:
                answer.pop()
        else:
            answer.remove([frame[0], frame[1], frame[2]])
            if check(answer) == False:
                answer.append([frame[0], frame[1], frame[2]])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))