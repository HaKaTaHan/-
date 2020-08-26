def solution(board):
    answer = 0
    maxP = 0
    temp = 0
    for i in board:
        temp += sum(i)
    
    if temp == 0:
        return 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                if maxP < board[i][j]:
                    maxP = board[i][j]

    if maxP == 0:
        answer = 1
    else:
        answer = maxP ** 2

    return answer

# 이전에 정사각형이 되는 변을 더한다 DP
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))