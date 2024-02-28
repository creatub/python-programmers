#모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
#모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 
#지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

def solution(sizes):
    minV, maxV = 0, 0 # 작은 숫자와 큰 숫자를 구분해서 비교
    for i in sizes:
        minV = minV if minV>min(i) else min(i) # 각 배열마다 작은 숫자 중 가장 큰 숫자 고름
        maxV = maxV if maxV>max(i) else max(i) # 각 배열마다 큰 숫자 중 가장 큰 숫자 고름
    return minV*maxV