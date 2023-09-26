def solution(n, t, m, p):
    arr = []
    answer = ''
    
    def change(n, base):
        if n == 0:
            return '0'

        result = ''
        while n:
            n, remainder = divmod(n, base)
            if remainder < 10:
                result = str(remainder) + result
            else:
                result = chr(remainder + 55) + result 
        return result

            
    num = 0
    while len(arr) <= m*t:
        now = change(num, n)
        num += 1
        arr += list(now)
    
    for i in range(p - 1, len(arr), m):
        if len(answer) == t:
            break
        answer += arr[i]
    return answer