#컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
## 재귀함수를 쓰지 않고 뇌지컬로 풀어본 문제 => 뭐가 문제인지 아직 파악하지 못
def solution(n, computers):
    answer = n # 전체가 각각의 네트워크를 가졌다고 가정
    idx = 0
    network_found=0
    network ={}
    network[0]=[0]
    #### 1차로 같은 네트워크끼리 묶어 network dictionary에 저장 - 중복체크 X
    for i in range(n): # 컴퓨터 대수만큼 array 전체 탐색
        for j in range(n):
            if computers[i][j]==1: # 동일 네트워크일 경우
                for key in network.keys(): # dictionary에 있는지 확인
                    if i in network[key]: # 탐색 중인 row가 있으면 
                        network_found = 1 # 네트워크 할당된 것을 확인
                        if j not in network[key]: # row는 있는데 column이 없으면 
                            network[key].append(j) # 해당 네트워크 신규 추가
                            answer-=1 # 네트워크 개수가 1개 감소 : 합쳐졌으므로
                        
                if network_found == 0: # 할당된 네트워크를 찾지 못할 경우
                    idx += 1 # 새로운 network에 등록
                    network[idx] = [i] # 네트워크에 신규 등록
                    if i!=j: # j도 등록되지 않았다면
                        network[idx].append(j) # 얘도 등록
                        answer-=1 # 네트워크 개수는 줄어듦
                network_found = 0 # network_found 초기화
    print(network.keys())
    print(network.values())
    print(answer)
    #### 중복체크
    checked_list=[]
    merged_list=[]
    for key_1 in network.keys(): # key를 전체 탐색하기 위해 for문
        checked_list.append(key_1) # 같은 key name끼리는 탐색하지 않기 위해 추가
        if key_1 in merged_list: # 이미 merge된 key일 경우 skip
            continue
        for key_2 in network.keys():
            if key_2 in checked_list: # key_1으로 이미 체크한 key라면 skip
                continue
            if [x for x in network[key_1] if x in network[key_2]]: # 중복된 value가 있다면
                answer-=1 # 네트워크 수를 하나 줄이고
                merged_list.append(key_2) # merge
        
    return answer


    
