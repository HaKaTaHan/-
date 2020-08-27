class Song(object):
    def __init__(self, name, time, seq):
        self.name = name
        self.time = time
        self.seq = seq

def trans(x):
    v = {"C": "H", "D": "J", "E": "L", "F": "M", "G": "P", "A": "R", "B": "T"}
    vc = {"C#": "I", "D#": "K", "F#": "O", "G#": "Q", "A#": "S"}
    
    for i in vc.keys():
        x = x.replace(i, vc.get(i))

    for i in v.keys():
        x = x.replace(i, v.get(i))

    return x

from datetime import datetime
def solution(m, musicinfos):
    answer = ''
    FMT = "%H:%M"
    arr = []
    m = trans(m)

    for i, j in enumerate(musicinfos):
        temp = j.split(",")

        temp[3] = trans(temp[3])

        t = datetime.strptime(temp[1], FMT) - datetime.strptime(temp[0], FMT)
        _min = t.seconds // 60

        l = len(temp[3])

        if _min < l:
            temp[3] = temp[3][:_min]
        else:
            temp[3] = temp[3] * (_min // l) + temp[3][:(_min % l)]
        if m in temp[3]:
            song = Song(temp[2], t.seconds, i)
            arr.append(song)

    if len(arr) == 0:
        return "(None)"
    else:
        arr.sort(key=lambda Song: (Song.time, -Song.seq))
        test = arr[0].name     
        answer = arr.pop().name

    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC#", ["12:00,12:14,HELLO,CDEFGAB"]))
print(solution("ABCDEFG", ["13:00,13:14,WORLD,CDEFGAB", "12:00,12:14,HELLO,CDEFGAB"]))

