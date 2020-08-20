def solution(nums):

    l = len(nums) // 2

    nums = list(set(nums))

    if len(nums) < l:
        return len(nums)
    else:
        return l

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
