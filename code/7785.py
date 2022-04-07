## 실버5
# 딕셔너리 사용
# 리스트 사용하면 O(n) 발생해서 for문까지 O(n^2)

import sys

n = int(input())

list = {}
for i in range(n) :
    name, state = sys.stdin.readline().split()

    if(state == "enter") :
        list[name] = True
    else :
        del list[name]
        
a = sorted(list.keys(), reverse=True)

for i in a :
    print(i)