# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:15:39 2024

@author: rlatk
"""

# 2번 문제 [단어 교환]

# =======================설명=========================
# find나 count나 remove를 사용하여 푼 사람들은 다 틀린 것

# set으로 접근해야 함 => index가 없어도 되기 때문에
# set.remove / set.add => O(1)
# list => O(N)

# insert, remove는 정말 비효율적인 메서드이다

# set과 list의 차이가 무엇일까?

#====================정해 코드====================
N,M = map(int,input().split())
A = set(map(str,input().split())) # 탐색 속도를 O(1)로 줄이는 전략
B = set(map(str,input().split()))

for _ in range(M):
    chA, chB = map(str, input().split())
    if chA in A and chB in B:
        A.remove(chA)
        B.remove(chB)
        A.add(chA)
        B.add(chB)
        
A = list(A)
A.sort()

print(*A)

#====================내가 짠 코드====================
# 30점/100점 => set을 쓰지 않고 list를 썼기 때문
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input를 각각 array length, iteration num으로 저장
user_input = input()
arr_len, iter_num = user_input.split(' ')
arr_len, iter_num = int(arr_len), int(iter_num)

a, b = [], [] # a b array 선언
# a array 저장
user_input = input()
a = user_input.split(' ')
# b array 저장
user_input = input()
b = user_input.split(' ')

# 교환 시작
for i in range(iter_num):
	user_input = input()
	ai, bi = user_input.split(' ')
	if ai in a and bi in b: # 각각이 a와 b에 있으면
		a = [x for x in a if x!=ai] # a에서 ai 제거
		b = [x for x in b if x!=bi] # b에서 bi 제거
		a.append(bi) # a에 bi 추가
		b.append(ai) # b에 ai 추가
a.sort() # 알파벳 순서대로
a_str = a[0] # 출력하기 위해 string 생성
for i in a[1:]:
	a_str += " "+i
print(a_str) # 결과 출력
	