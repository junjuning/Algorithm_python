from collections import Counter
def solution(array):
    array = "".join(map(str, array))
    cnt = Counter(array)
    return cnt['7']