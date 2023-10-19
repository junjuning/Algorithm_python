
def divide(string):
    left = 0
    right = 0
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return string[:i + 1], string[i + 1:]

def is_right(string):
    q = []
    for i in string:
        if i == "(":
            q.append("(")
        else:
            if not q:
                return 0
            q.pop()
    return 1
    
def solution(p):
    answer = ''
    if not p:
        return ""
    
    u, v = divide(p)
    
    if is_right(u) == 1:
         return u + solution(v)
        
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer