def solution(numbers):
    answer = []
    
    for i in numbers:
        num = list(bin(i)[2:])
        num.reverse()

        if i % 2 == 0:
            num[0] = '1'
        else: 
            for j in range(len(num)):
                if num[j] == '0':
                    num[j] = '1'
                    num[j - 1] = '0'
                    break
                if j == len(num) - 1:
                    num[j] = '0'
                    num.append('1')
        num.reverse()
        answer.append(int(''.join(num), 2))
        
    return answer
