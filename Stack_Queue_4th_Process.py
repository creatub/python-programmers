#프로세스
#현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities): # 첫 순서가 우선순위가 제일 높으면
            answer+=1 # 실행 순서에 1을 더하고
            if location==0: # target location이 0이라면
                break; # 루프를 멈춘다.
            else: # target location이 0이 아니라면 1 이상인 것으로
                priorities=priorities[1:] # 맨 앞 프로세스를 없애고
                location-=1 # 위치를 앞으로 한 칸 당겨온다
        else: # 첫 프로세스의 우선순위가 제일 높지 않다면
            priorities = priorities[1:]+[priorities[0]] # 첫 프로세스만 맨 뒤로 보내고 
            if location == 0: # 그게 target이었다면
                location = len(priorities)-1 # 맨 뒤 번호를 부여한다.
            else: # target이 아니었다면
                location-=1 # target을 한 칸 당겨온다.
    return answer
