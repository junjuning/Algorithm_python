n = int(input())
arr = [1, 1]

for i in range(2, n):
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[n-1])
            



# 1
# 10 
# 100 101
# 1000 1001 1010 
# 10000 10001 10010 10101 10100
# 
# 