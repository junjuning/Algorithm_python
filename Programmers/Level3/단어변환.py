from collections import deque
def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    
    if target not in words:
        return 0
    
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        
        for word in words:
            diff = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])