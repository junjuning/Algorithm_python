from math import gcd
def solution(arr):
    answer = 0

    for i in range(1, len(arr)):
        arr[i] = arr[i] * arr[i-1] // gcd(arr[i], arr[i-1])
        
    return arr[-1]