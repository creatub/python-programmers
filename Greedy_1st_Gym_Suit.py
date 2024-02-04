def solution(n, lost, reserve):
    answer = 0
    del_lst = []
    for i in reserve: #여벌 있는 사람 중
        if i in lost: # 잃어버린 사람이 있다면
            del_lst.append(i)      
    for i in del_lst:
        reserve.remove(i) # reserve 배열에서 제거
        lost.remove(i) # lost에서도 제거
        
    idx = 1 # 학생 번호 1번부터 시작
    while idx <= n:
        if idx in lost: # 학생 번호가 lost에 있을 경우
            if idx-1 in reserve: # 이전 번호에 여분이 있다면
                answer += 1 # ans 1 더하고
                reserve.remove(idx-1) # 여분 배열에서 삭제
            elif idx+1 in reserve: # 다음 번호에 여분이 있다면
                answer += 1 # ans 1 더하고
                reserve.remove(idx+1) # 여분 배열에서 삭제
        else: # 학생 번호가 lost에 없을 경우
            answer += 1 # ans 1 더하기
        idx += 1 # 학생 번호 +1
            
    return answer
