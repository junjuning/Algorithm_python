def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = set(nums)
    m = len(nums)
    
    if n <= m:
        return n
    else:
        return m