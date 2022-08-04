# 구글링해서 푼 문제,,
# 집합 set 사용, set은 중복x, in 탐색 효율 높음

def solution(N, number):
    if(N == number):
        return 1
    dp = [set() for i in range(9)] 
    # N을 i개로 포현하는 수들의 집합
    for i in range(1, 9): # N이 i개 일 때
        dp[i].add(int(str(N)*i)) # 일단 숫자가 i개 사용된 숫자 넣기 ex)1, 11, 111...
        for j in range(i//2 + 1): # f(4)=f(1)+f(3) 합 f(2)+f(2) 합 f(3)+f(1)
            for first in dp[j]: 
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0 :
                        dp[i].add(first // second)
                    if first != 0 :
                        dp[i].add(second // first)
        if number in dp[i]: # 연산값이 number와 일치하는 개수 return
            return i
    return -1 # 숫자가 8개 넘어가면 -1 return