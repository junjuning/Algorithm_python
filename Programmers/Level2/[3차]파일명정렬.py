import re

def solution(files):
    arr = []
    
    for file in files:
        arr.append(re.split(r"([0-9]+)", file))
    sort = sorted(arr, key = lambda x: (x[0].lower(), int(x[1])))
        
    return [''.join(s) for s in sort]