from copy import deepcopy

def rotate(arr, m):
    res = []
    temp = [[0 for col in range(m)]for row in range(m)]

    for n in range(3):
        for i in range(m):
            for j in range(m):
                temp[j][m-i-1] = arr[i][j]
        arr = deepcopy(temp)
        res.append(arr)

    return res

def check(key, lock, M, N):
    res = False
    count = N + M -1

    for i in range(count):
        for j in range(count):
            tempLock = deepcopy(lock)
            move(tempLock, key, i, j, M)
            if lockCheck(tempLock, N, M):
                return True

    return res

def move(lock, key, p, q, m):
    for i in range(m):
        for j in range(m):
            lock[i+p][j+q] += key[i][j]

def lockCheck(lock, n, m):
    res = True
    
    for i in range(m-1, n+(m-1)):
        for j in range(m-1, n+(m-1)):
            if lock[i][j] != 1:
                return False

    return res

def lockInit(lock, N, M):
    res = [[0 for col in range(N + 2*(M-1))] for row in range(N + 2*(M-1))]

    for i in range(M-1, N+(M-1)):
        for j in range(M-1, N+(M-1)):
            res[i][j] = lock[i-(M-1)][j-(M-1)]

    return res

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    candidateKey = [key]

    candidateKey += rotate(key, M)
    lock = lockInit(lock, N, M)

    for i in range(4):
        if check(candidateKey[i], lock, M, N):
            return True
        
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

