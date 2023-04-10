def solution(phone_book):
    phone_book.sort() #문자열이니까 사전순 정렬될 것
    prev = phone_book[0]
    for ph in range(1, len(phone_book)) :
        if phone_book[ph].find(prev) == 0 :
            return False
        prev = phone_book[ph]
    return True
