from collections import deque

def solution(s):
    answer = []
    num = 0
    cnt = 0
    
    while s != '1':
        cnt += 1

        # while '0' in s:
        #     s = s.replace('0', '', 1)
        #     num += 1
        
        num += s.count('0')
        s = s.replace('0', '')
        c = len(str(s))
        s = format(c, 'b')

    return [cnt, num]