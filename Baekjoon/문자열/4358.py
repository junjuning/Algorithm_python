import sys
dic = {}
total = 0
while True:
    total += 1
    string = sys.stdin.readline().strip()
    if string == '':
        break

    if(string not in dic):
        dic[string] = 1
    else:
        dic[string] += 1

dic = sorted(dic.items())

for tree, num in dic:
    print('%s %.4f' %(tree, num/(total-1)*100))