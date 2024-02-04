# 같은 숫자는 싫어
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

def solution(arr):
    answer = []
    prev_val = -1; #연속된 값을 비교하기 위한 value 
    for i in arr:
        if i == prev_val:
            continue
        else:
            prev_val = i
            answer.append(i)
    return answer
##정확성 71.9, 효율성 28.1
