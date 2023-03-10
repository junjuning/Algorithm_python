def solution(n, k):
    answer = 0

    def isPrime(x):
        for i in range(2, int(x**(1/2)+1)):
            if x % i == 0:
                return False
        return True

    arr = []
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    result = result[::-1]
    
    
    arr = list(result.split('0'))

    for i in arr:
        if i == '' or i == '1':
            continue
        if isPrime(int(i)):
            answer += 1


    return answer