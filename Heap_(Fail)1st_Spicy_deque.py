# heapq 문제를 deque로 풀었을 때 - 속도는 안나지만 답은 나오긴 함
# 효율성 체크에서 런타임 오버로 실
from collections import deque

def solution(scoville, K):
    scoville.sort()
    dq = deque(scoville)
    answer = 0
    while any(x<K for x in dq):
        if len(dq) <= 1:
            return -1
        i = dq.popleft()
        dq[0] = i + dq[0]*2
        dq = deque(sorted(dq))
        answer += 1
    
    return answer
