import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))

max = []

print(0, end=' ')
max.append(0) 
max.append(tower[0]) 

for i in range(1, n):
    if(max[1]<tower[i]):
        max.clear()
        max.append(i)
        max.append(tower[i])
        print(0, end=' ')
    else:
        len2 = int(len(max)/2)
       
        while(len2 >= 1):
            if(max[len2*2-1] < tower[i]):
                max.pop()
                max.pop()
            elif(max[len2*2-1] > tower[i]):
                print(max[len2*2-2]+1, end=' ')
                max.append(i)
                max.append(tower[i])
                break
            len2-=1