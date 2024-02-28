# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:52:19 2024

@author: rlatk
"""

# 3번 문제 [도형수]

# N 1~500 완전탐색
# 500~2000 BFS/DFS
# 2000~5000 DP
# 5000이상 => 수학문제 (못푸는 수학문제)

# 탐색은 deque로 해야한다. 데이터 추가/제거가 활발하게 이뤄지기 때문
# index가 필요한 것 중에 deque만큼 좋은 게 없음

#====================정해 코드 ====================
import sys
from collections import deque
input = sys.stdin.readline()

N = int(input())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 방문 기록을 저장할 변수
visited = [[False for _ in range(N)] for _ in range(N)]

# 최대 도형 수를 저장할 변수
result = [0,0,0,0,0,0,0,0,0,0,0]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#탐색 시작 위치 찾기
for i in range(N):
    for j in range(N):
        if not visited[i][j]: #방문한 적이 없는 곳이 바로 탐색 시작 위치
            target = matrix[i][j]
            q = deque()
            q.append([i,j])
            visited[i][j] = True
            cnt = 1 #매 도형 수의 크기를 측정
            
# 탐색 시작
while q:
    cx, cy = q.popleft() # DFS
    for k in range(4):
        nx = cx+dx[k]
        ny = cy+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if not visited[nx][ny] and matrix[nx][ny]==target:
                q.append([nx,ny])
                visited[nx][ny]=True
                cnt+=1
    #최대 도형 수 갱신
    if result[target] < cnt:
        result[target] = cnt

answer = ''.join(map(str,result[1:]))
print(answer)
        


#====================내가 짠 코드====================
# 88점/100점


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
user_input = input()
n = int(user_input)
n_array = []
for i in range(n):
	user_input = input()
	n_array.append([int(x) for x in user_input.split(' ')])

	
def dfs(arr, visited, row, col, val, group):
	if row <0 or row>=len(arr) or col<0 or col>=len(arr[0]) or arr[row][col] != val or visited[row][col]:
		return 0
	visited[row][col]=True
	size = 1
	
	size += dfs(arr, visited, row-1, col, val, group)
	size += dfs(arr, visited, row+1, col, val, group)
	size += dfs(arr, visited, row, col-1, val, group)
	size += dfs(arr, visited, row, col+1, val, group)
	
	return size

def cnt_largest_group(n, arr, target):
	visited = [[False]*n for _ in range(n)]
	max_size = 0
	
	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				group_size = dfs(arr,visited,i,j,target,0)
				max_size = max(max_size,group_size)
	return max_size

answer = ""
for i in range(10):
	# if i+1 in n_array:
		answer += str(cnt_largest_group(n,n_array, i+1)) + " "
	# else:
	# 	if i==n-1:
	# 		answer += "0"
	# 	else:
	# 		answer += "0 "
print(answer)