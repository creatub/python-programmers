# 해 - 전화번호 목록
# 그냥 개념적으로 접근했으나 phone_book size가 커지면 실행시간 초과됨 -> 어떻게 풀었는지 기억이 안남
# 복습 필요
def solution(phone_book):
    answer = True
    for i in phone_book:
        for j in phone_book:
            if(i!=j and len(j)>=len(i)):
                if(j[0:len(i)]==i):
                    answer = False
                    break
    return answer
