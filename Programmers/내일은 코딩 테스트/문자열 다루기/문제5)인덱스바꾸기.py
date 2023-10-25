def solution(my_string, num1, num2):
    my_string = list(my_string)
    
    key1 = my_string[num1]
    key2 = my_string[num2]
    my_string[num1] = key2
    my_string[num2] = key1
    
    return ''.join(my_string)