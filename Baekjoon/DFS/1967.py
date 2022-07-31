import sys

n = int(input())
tree = []
global cnt
cnt=0

def dfs(x):
    for i in range(n-1) :
        if(tree[i][0]==x):
            dfs(tree[i][1])
            cnt+=tree[i][2]

for i in range(n-1):
    tree.append(list(map(int, sys.stdin.readline().split())))

count = []
for i in range(n-1):
    if(tree[i][0]==1):
        cnt=tree[i][2]
        dfs(tree[i][1])
        count.append(cnt)
        
print(max(count))