import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K:
        if len(scoville)==1:
            answer=-1
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        answer+=1
    
    return answer
