def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    
    return answer
"""
그냥 문자열로 하고 reverse 정렬을 하면 9, 5, 34, 30, 3이다
안타깝게도 9534330일 때 가장 크다.
문자 3이 문자 30보다 더 크면 가능할 것 같다.
1000이하 수자라는 조건이 있기에 모든 문자를 4자리로 만들어본다
각 문자에 같은 문자를 여러번 곱하면 원하는 순으로 크기 비교가 가능하다.
"""
print(solution([3,30,34,5,9]))
print(solution([121,11]))
print(solution([1,112]))