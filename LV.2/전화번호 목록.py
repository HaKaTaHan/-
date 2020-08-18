def solution(phone_book):
    answer = True

    for i, j in enumerate(phone_book):
        for k in range(i+1, len(phone_book)):
            if len(j) > len(phone_book[k][:len(j)]):
                if phone_book[k] == j[:len(phone_book[k])]:
                    answer = False
                    break
            else:
                if j == phone_book[k][:len(j)]:
                    answer = False
                    break
        if answer == False:
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["4321","432"]))
