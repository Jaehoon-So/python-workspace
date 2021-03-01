from random import *

lstid = range(1, 21) # 1부터 20까지 숫자를 생성
lstid = list(lstid)
shuffle(lstid)

print("-- 당첨자 발표 --")
chicken = sample(lstid, 1)
print("치킨 당첨자 : " + str(chicken[0]))

lstid = set(lstid)
chicken = set(chicken)

lstid = lstid - chicken
lstid = list(lstid)
coffee = sample(lstid, 3)

print("커피 당첨자 : " + str(coffee))
print("-- 축하합니다 --")

# 한번에 4명을 뽑는 방법도 있다.