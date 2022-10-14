import sys

s = list(sys.stdin.readline().strip())


arr = []
for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        arr.append(''.join(s[j:j+i]))
        
    
print(len(set(arr)))