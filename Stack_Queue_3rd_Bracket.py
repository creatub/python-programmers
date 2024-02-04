# 올바른 괄호
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    answer = True
    num_starter = 0 # (의 개수
    num_ender = 0 # )의 개수
    for i in s: 
        if i == "(":
            num_starter +=1
        else:
            num_ender +=1
        if num_ender > num_starter: # )가 (보다 많으면 잘못된 패턴
            answer=False
            break
    if num_starter != num_ender: # 마지막에 개수가 다르면 잘못된 패턴
        answer=False

    return answer
