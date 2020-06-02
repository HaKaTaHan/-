"""
스택 냄새 남
주어진 이차원 배열이 세로로 봐야되어서 세로로 먼저 쪼갬
그 이후는 단순 baguni랑 비교
예외로는 인형이 비어있는 부분은 보지 않는 처리와
처음 바구니는 비어 있기에 무조건 인형 넣어주는 처리함
"""
def solution(board, moves):
    answer = 0

    n = len(board)

    switch = []
    baguni = []

    for i in range(n):
        temp = []
        for j in range(n):
            if board[j][i] != 0:
                temp.append(board[j][i])
        switch.append(temp[::-1])

    for i in moves:
        if len(switch[i-1]) == 0:
            continue

        temp = switch[i-1].pop()

        if len(baguni) == 0 :
            baguni.append(temp)
        elif temp == baguni[-1]:
            baguni.pop()
            answer = answer + 1
        elif temp != baguni[-1]:
            baguni.append(temp)

    return answer * 2


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

