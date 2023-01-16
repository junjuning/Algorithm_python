## 실버 3

t = int(input())

def fibonacci(n):
    if(n >= 3):
        for i in range(2, n):
            zero.append(zero[i - 1] + zero[i])
            one.append(one[i - 1] + one[i])
    print(zero[n], one[n])

for i in range(t):
    n = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    fibonacci(n)