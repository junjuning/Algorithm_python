# 다중집합
# 구현안하고 counter 이용하면 됨

from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = []
    arr2 = []
    
    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90:
            arr1.append(str1[i] + str1[i + 1])
    
    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90:
            arr2.append(str2[i] + str2[i + 1])

    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    add = list((c1 | c2).elements())
    min = list((c1 & c2).elements())
    
#     arr1_temp = arr1.copy()
#     add = arr1.copy()

#     for i in arr2:
#         if i not in arr1_temp:
#                 add.append(i)
#         else:
#             arr1_temp.remove(i)
    
#     min = []
#     for i in arr2:
#         if i in arr1:
#             arr1.remove(i)
#             min.append(i)
    
    if len(add) == 0:
        return 65536

    return int((len(min) / len(add)) * 65536)