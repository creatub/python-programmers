def solution(name):
    answer = 0
    ## 알파벳을 이동하는 동작 수
    for c in name:
        answer+= min(ord(c)-65, 91-ord(c))
    ## A가 아닌 index 배열로 추출
    hopping_index = [x for x in range(len(name)) if name[x]!="A"]
    way1 = hopping_index[-1] # 정방향으로 갔을 경우
    way2 = len(name)-hopping_index[0] # 역방향으로 갔을 경우
    add = min(way1, way2)
    for i in range(len(hopping_index)-1): # detour하는 경우
        way1 = hopping_index[i]*2 + len(name)-hopping_index[i+1] # 정방향 detour
        way2 = hopping_index[i] + (len(name)-hopping_index[i+1])*2 # 역방향 detour
        add = min(add, way1, way2)
    answer += add
    return answer
