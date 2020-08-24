class Memeber(object):
    def __init__(self, uid, nickname):
        self.uid = uid
        self.nickname = nickname

def solution(record):
    answer = []
    rec = []
    enter = "님이 들어왔습니다."
    leave = "님이 나갔습니다."
    
    members = {}

    for i in record:
        i = i.split()
        
        rec.append([i[0], i[1]])

        if i[0] == "Enter":
            members[i[1]] = Memeber(i[1], i[2])
        elif i[0] == "Change":
            temp = members.get(i[1])
            temp.nickname = i[2]
            members[i[1]] = temp

    for j in rec:
        temp = ""
        member = members.get(j[1])
        if j[0] == "Enter":
            temp = member.nickname + enter
            answer.append(temp)
        elif j[0] == "Leave":
            temp = member.nickname + leave
            answer.append(temp)

        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))