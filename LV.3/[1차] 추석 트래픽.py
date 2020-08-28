class TimeLog(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def solution(lines):
    answer = 0
    arrTime = []

    for line in lines:
        line = line.split()

        s = line[1].split(":")
        t = line[2][:-1]

        sMilsec = int((int(s[0]) * 60 * 60 + int(s[1]) * 60 + float(s[2])) * 1000)
        tMilsec = int(float(t) * 1000)

        arrTime.append(TimeLog(sMilsec-tMilsec+1, sMilsec))

    for i in arrTime:
        count = 0
        start = i.end
        end = start + 999

        for j in arrTime:
            if j.end - start >= 0 and end - j.start >= 0:
                count += 1
            # for k in range(start, end+1):
            #     if k in [x for x in range(j.start, j.end)]:
            #         count += 1
            #         break
            

        if count > answer:
            answer = count

    return answer

# print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))

