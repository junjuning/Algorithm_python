# 해시
# 해시고 뭐고 내 맘대로 푼 문제

def solution(nums):
    answer = 0
    setNums = set(nums)
    newNums = list(setNums)
    
    if(len(nums)//2 < len(newNums)):
        answer = len(nums)//2
    else:
        answer = len(newNums)
    return answer