#기능 개발
#프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

def solution(progresses, speeds):
    answer = []
    while len(progresses)!=0: # progresses 배열을 줄여나가면서 시행
        progresses=[p + s for p, s in zip(progresses, speeds)] # p와 s의 요소별 합 저장
        if progresses[0]>=100: # 첫 번째 요소가 100이상일 때만 시행
            ans=0 # 배포 개수 초기화
            for i in range(len(progresses)): # progresses의 길이만큼 for문
                if progresses[i]>=100: # 100이상인 개수를 count
                    ans+=1
                else:# 100미만인 곳에서 break
                    break 
            progresses=progresses[ans:] # progresses 배열을 100미만인 곳부터로 재할당
            speeds=speeds[ans:] # speeds 배열도 재할당
            answer.append(ans) # 배포 개수 추가
    return answer
