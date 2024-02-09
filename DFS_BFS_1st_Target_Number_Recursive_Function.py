#타겟 넘버
#사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#뇌지컬로 풀었으나 수행시간이 너무 오래 걸려 타임오버.. 재귀함수로 풀어야 함
def solution(numbers, target):
    answer = 0
    answer = f(0,0,numbers, target,answer) # f function 호출
    return answer

def f(sum, n, numbers, target, answer):
    if n==len(numbers): # numbers 마지막 index까지 도달 시
        if sum==target: # 총 합계가 target과 같으면
            answer+=1 # 적합한 방법으로 합산
    else: # 혹은 다음 숫자를 + - 각각의 경우로 sum에 더하여 재귀함수 수행
        answer=f(sum+numbers[n], n+1, numbers, target, answer)
        answer=f(sum-numbers[n], n+1, numbers, target, answer)
    return answer
