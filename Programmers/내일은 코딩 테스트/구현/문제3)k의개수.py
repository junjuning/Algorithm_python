import re
from collections import Counter
def solution(i, j, k):
    answer = 0
    
    string = ""

    for a in range(i, j + 1):
        string += str(a)
    
    string = re.split("([0-9])", string)
    string = list(filter(lambda x: x != "", string))

    string = Counter(string)
    return string[str(k)]
