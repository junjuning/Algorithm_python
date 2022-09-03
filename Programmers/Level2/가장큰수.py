# 구글링함
# 람다함수,,써야할 줄은 상상도 못했지

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

solution([6, 10, 2])