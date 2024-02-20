def solution(maps):
    answer = findRoute(0,0,maps,1, [])
    shortest = min(answer) if answer else -1
    return shortest

def findRoute(x, y, maps, cnt, answer):
    if cnt < len(maps) * len(maps[0]):
        if x==len(maps)-1 and y==len(maps[0])-1:
            answer.append(cnt)
            return answer
        else:
            if x+1<len(maps) and maps[x+1][y]:
                maps[x+1][y] = 0
                answer = findRoute(x+1, y, maps, cnt+1, answer)
                maps[x+1][y] = 1
            if x>0 and maps[x-1][y]:
                maps[x-1][y] = 0
                answer = findRoute(x-1, y, maps, cnt+1, answer)
                maps[x-1][y] = 1
            if y+1<len(maps[0]) and maps[x][y+1]:
                maps[x][y+1]=0
                answer = findRoute(x, y+1, maps, cnt+1, answer) 
                maps[x][y+1]=1
            if y>0 and maps[x][y-1]:
                maps[x][y-1]=0
                answer = findRoute(x, y-1, maps, cnt+1, answer) 
                maps[x][y-1]=1
    return answer
