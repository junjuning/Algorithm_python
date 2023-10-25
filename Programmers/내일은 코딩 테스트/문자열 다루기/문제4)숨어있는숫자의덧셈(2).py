# 정규표현식, findAll, \d+ -> 숫자

import re
def solution(my_string):
    numArr = list(map(int, re.findall("\d+", my_string)))
    return sum(numArr)