from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    result = list(p - c)
    return result[0]