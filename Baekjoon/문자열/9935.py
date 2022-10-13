## 골드4
# replace 사용하니까 시간초과

import sys
string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

arr = []
size = len(boom)
for i in string:
    arr.append(i)
    if(i == boom[-1] and ''.join(arr[-size:])== boom):
        del arr[-size:]
        
if(not arr):
    print('FRULA')
else:
    print(''.join(arr))
    
# import sys

# string = sys.stdin.readline().strip()
# boom = sys.stdin.readline().strip()

# while (boom in string):
#     string = string.replace(boom, '')
    
# if(not string):
#     print("FRULA")
# else:
#     print(string)

