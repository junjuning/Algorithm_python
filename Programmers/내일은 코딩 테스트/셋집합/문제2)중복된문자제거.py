from collections import Counter
def solution(my_string):
    answer = ''
    my_string = dict(Counter(my_string))
    my_string = list(my_string.keys())
    return ''.join(my_string)