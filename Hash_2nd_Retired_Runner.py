#해시 level1_ 완주하지 못한 선수

#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
#완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
#완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


def solution(participant, completion):
    participant.sort() # 문자 순서대로 sort
    completion.sort()
    answer = ""
    for i in range(len(completion)): # 순서대로 탐색
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == "": # 끝까지 없다면 참가자 마지막 사람이 return됨
        answer = participant[-1]
    return answer