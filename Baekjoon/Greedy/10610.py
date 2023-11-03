n = input()
n = list(map(int, n))
n.sort(reverse = True)
cal = sum(n)
if n[-1] != 0:
    print(-1)

elif cal % 3 == 0:
    n = list(map(str, n))
    print(''.join(n))
    
else:
    print(-1)