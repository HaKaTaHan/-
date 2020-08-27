class File(object):
    def __init__(self, head, number, fullName, seq):
        self.head = head
        self.number = number
        self.fullName = fullName
        self.seq = seq

def makeHead(x):
    res = ""
    idx = 0
    
    for i in range(len(x)):
        if x[i].isdigit():
            idx = i
            break
        else:
            res += x[i]

    return res, idx

def makeNumber(x):
    res = ""

    for i in range(len(x)):
        if not x[i].isdigit():
            break
        else:
            res += x[i]

    return res

def solution(files):
    answer = []
    arr = []

    for i, _file in enumerate(files):
        head = ""
        number = ""
        idx = 0
        head, idx = makeHead(_file)
        number = makeNumber(_file[idx:])
        
        f = File(head.lower(), int(number), _file, i)

        arr.append(f)

    arr.sort(key=lambda f: (f.head, f.number, f.seq))

    for i in arr:
        answer.append(i.fullName)

    return answer
"""
import re
def solution(files):
    file_lst = [re.split('([0-9]+)',i) for i in files]
    file_lst.sort( key = lambda x : ( x[0].lower(), int(x[1]) ) )
    print(file_lst)
    return [''.join(lst) for lst in file_lst]
"""
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["img12.png", "img012.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "F-5 AAAA Fighter"]))
