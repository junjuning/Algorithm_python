from collections import Counter
def solution(gems):
    num = len(set(gems))
    counter = Counter(gems[:num - 1])
    answer = []
    min = len(gems)
    left = 0
    
    for right in range(num - 1, len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            if min > right - left:
                min = right - left
                answer = [left, right]
            
    return answer
