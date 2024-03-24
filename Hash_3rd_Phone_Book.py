def solution(phone_book):
    answer = True 
    phone_book.sort() # sort하면 바로 다음 string이 이전 string을 포함하는 경우만 접두사인 경우
    for idx in range(len(phone_book)-1):
        if(len(phone_book[idx+1])>=len(phone_book[idx])):
            if(phone_book[idx]==phone_book[idx+1][0:len(phone_book[idx])]):
                answer=False
                break
    return answer
