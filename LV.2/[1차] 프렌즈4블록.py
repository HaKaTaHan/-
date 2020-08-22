def search(row, col, matrix, remove):
    one = matrix[row][col]
    two = matrix[row][col+1]
    three = matrix[row+1][col]
    four = matrix[row+1][col+1]

    res = set([one, two, three, four])

    if len(res) == 1 and res.pop() != "":
        remove.add((row, col))
        remove.add((row, col+1))
        remove.add((row+1, col))
        remove.add((row+1, col+1))
    
    return remove

def solution(m, n, board):
    answer = 0
    matrix = [["" for col in range(n)]for row in range(m)]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = board[i][j]

    while True:
        remove = set()

        for i in range(m-1):
            for j in range(n-1):
                remove = search(i, j, matrix, remove)
        
        if len(remove) == 0:
            break

        for i in list(remove):
            matrix[i[0]][i[1]] = ""
            answer += 1

        for i in range(m-1, -1, -1):
            for j in range(n):
                if matrix[i][j] == "":
                    for k in range(i-1, -1, -1):
                        if matrix[k][j] != "":
                            matrix[i][j] = matrix[k][j]
                            matrix[k][j] = ""
                            break


    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(2,2,["AA","AA"]))
print(solution(4,4,["ABCD", "BACE", "BCDD", "BCDD"]))
