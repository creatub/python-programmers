def solution(name):
    answer = 0
    ## 알파벳을 이동하는 동작 수
    for c in name:
        answer+= min(ord(c)-65, 91-ord(c))
    
    ## 거쳐갈 필요 없는 A가 있을 경우의 계산
    a_series_len = 0 # 연속된 A가 가장 긴 길이 찾기
    for i in range(len(name)): # A 개수를 string length까지 늘려가며 탐색
        if "A"*(i+1) in name:
            a_series_len = i+1 # 가장 긴 A series의 길이 저장
    if a_series_len > 0:
        a_start = name.find("A"*a_series_len) # 가장 긴 A series의 첫 index 저장
        # 처음이나 중간에 가장 긴 A series가 있는 경우
        # detour1: 앞쪽부터 갔다가 뒤쪽으로 돌아가기
        detour1 = max(0,(a_start-1)*2) + (len(name)-a_start-a_series_len)
        # detour2: 뒤쪽부터 갔다가 앞쪽으로 돌아가기
        detour2 = (len(name)-a_start-a_series_len)*2 + (a_start-1)
        detour = min(detour1, detour2)
        if(a_start+a_series_len==len(name)): # 마지막에 가장 긴 A series가 있는 경우
            detour = max(0, a_start-1)
        if(name[1]=="A")
        # 정방향으로 쭉 갔을 때의 최소값 = len(name)-1
        answer += min(detour, len(name)-1)
    else:
        answer += len(name)-1
        
    return answer
