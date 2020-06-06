def solution(phone_number):
    answer = ['*' for i in range(len(phone_number) - 4)]
    
    return ''.join(answer) + phone_number[-4:]

print(solution("01033334444"))