# from collections import Counter을 사용하면 자동으로 세줌
# 시간복잡도 확 줄음

from collections import Counter
def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    counter = sorted (counter.values(), reverse = True)
    
    num = 0
    
    for i in range(len(counter)):
        num += counter[i]
        answer += 1
        if num >= k:
            return answer

# def solution(k, tangerine):
#     answer = 0
    
#     arr = [0 for _ in range(10000001)]
    
#     for i in tangerine:
#         arr[i] += 1
        
#     arr.sort(reverse = True)
    
#     num = 0
    
#     for i in range(len(arr)):
#         num += arr[i]
#         answer += 1
        
#         if num >= k:
#             return answer