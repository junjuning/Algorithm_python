from collections import deque
def solution(S):
    q = []
    answer = []
    num = 0
    right = 0
    
    for i in S:
        if i == ">":
            if q:
                right += 1

        elif i == "<":
            if right != 0:
                if len(q) > right:
                    #?를 right한테 줄수있는지
                    while len(q) > right:
                        now = q.pop()
                        if now == "?":
                            right += 1
                        else:
                            break
                    print((right - 1) * 2, "R")
                    answer.append(right*2)
                else:
                    print(len(q)*2, "l")
                    answer.append(len(q)*2)
                q = []
                right = 0
            q.append("<")
        else:
            q.append("?")
        print(q)
    
    print(max(answer))
    
solution("<<?>><<>?>>>??><")

