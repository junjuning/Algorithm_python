# 정규식 & 공백제거

import re
def solution(my_string):
    my_string = re.split("([^0-9])", my_string)
    op = ["+", "-"]
    my_string = list(filter(lambda x: x.strip() != "", my_string))
    answer = int(my_string[0])
    
    for i in range(1, len(my_string) - 1):
        if my_string[i] == "+":
            answer = answer + int(my_string[i + 1])
        elif my_string[i] == "-":
            answer = answer - int(my_string[i + 1])
    return answer