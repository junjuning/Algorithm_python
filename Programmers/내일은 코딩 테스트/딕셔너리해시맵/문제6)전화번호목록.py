def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        target = phone_book[i]
        if target == phone_book[i + 1][:len(target)]:
            return False
    
    return True