import random

#게임월드
GameWorld = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1]]

#시작위치
player = [0,0]

#번개 위치
thunder = [0,1]

#보물 위치
treasure = [2, 1]

#가능 액션 4가지(상하좌우) - 해당액션마다의 다음턴의 기대값을 알려주는 agent <- GameWorld랑 비교해
#방문한 곳은 False로, 방문하지 않은 곳은 True로 해서 재방문을 막을거임

#Agent = [GameWorld == [True], [True], [True], [True], [True], [True]]
Agent = [True, True, True, True, True, True]

print([Agent])
print([GameWorld])