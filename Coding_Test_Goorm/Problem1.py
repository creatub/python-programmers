# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1번 문제 [상자 채우고 비우기]
#====================정해코드====================
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
box = [0 for _ in range(N+1)] # N의 최대가 100이기 때문에 일반적인 배열로 선언

for _ in range(M):
    boxNumber, command, ballCnt = map(int, input().split())
    
    if command == 1:
        box[boxNumber] += ballCnt
    else:
        if box[boxNumber] > ballCnt:
            box[boxNumber] -= ballCnt
        
print(*box)


#====================내가 제출한 코드====================
# 100점/100점
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input을 각각 box num, iteration num으로 저장
user_input = input()
box_num, iter_num = user_input.split(' ')

# box 개수만큼 0으로 initialize
boxes = [0] * int(box_num)
	
# 공 채우고 비우기 시작
for i in range(int(iter_num)):
	box_input = input()
	box, order, num = box_input.split(' ')
	if int(order)==1: # 명령어가 1인 경우
		boxes[int(box)-1] += int(num) # 상자 숫자에 저장된 공의 개수를 증가
	else: # 명령어가 2인 경우
		if boxes[int(box)-1]<int(num): # 빼려는 숫자가 상자에 든 공 개수보다 높은 경우
			continue # 통과
		else: # 같거나 적으면 빼기
			boxes[int(box)-1] -= int(num)

			
for i in range(int(box_num)):
	print(boxes[i]) # 출력