from collections import Counter
def solution(array):
    count = Counter(array)
    
    count = list(sorted(count.items(), key = lambda x: x[1], reverse = True))
    key = count[0][0]
    value = count[0][1]
    
    for i, j in count:
        if j == value and i != key:
            return -1
    return key