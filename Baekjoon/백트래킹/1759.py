## 골드 5
# 백트래킹 응용

import sys

l, c = map(int, sys.stdin.readline().split())

arr = list(sys.stdin.readline().split())
vowel = ['a', 'e', 'i', 'o', 'u']
result = []

arr = sorted(arr)

def dfs(num):
    if(len(result) == l):
        if(1 <= len(set(vowel) & set(result)) <= l - 2):
            print(''.join(result))  
    else:
        for i in range(num, c):
            if(arr[i] not in result):
                result.append(arr[i])
                dfs(i)
                result.pop()

dfs(0)