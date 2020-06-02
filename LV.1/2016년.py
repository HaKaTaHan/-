import datetime

def solution(a, b):
    return datetime.datetime(2016, a, b).strftime('%c').upper()[:3]

print(solution(5, 24))