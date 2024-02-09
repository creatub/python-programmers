#타겟 넘버
#사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#뇌지컬로 풀었으나 수행시간이 너무 오래 걸려 타임오버.. 재귀함수로 풀어야 함
def solution(numbers, target):
    answer = 0
    num = 0
    if sum(numbers)>=target:
        for i in range(pow(2, len(numbers))):
            for j in range(len(numbers)):
                if i%(pow(2, j+1))>=pow(2,j):
                    num-=numbers[j]
                else:
                    num+=numbers[j]
            if num==target:
                answer+=1
            num=0
