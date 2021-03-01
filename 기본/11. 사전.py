cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

# get을 이용해 값을 가져오는 방법
print(cabinet.get(3))
# 대괄호를 이용해 없는 키를 출력하려고하면 오류가 난다.
# print(cabinet[5])
print(cabinet.get(5)) # None 값이 없으면 이런식으로 출력된다 get의 경우
print(cabinet.get(5, "사용 가능")) # 없을때의 기본값을 등록해줄 수 있다
print("hi")

# 사전자료형에 어떤 값이 있는지 확인하는 방법
print(3 in cabinet) # 3이라는 키가 cabinet에 있으면 True
print(5 in cabinet) # False

# 새 손님
print(cabinet)
cabinet[3] = "김종국" # 값이 갱신된다
cabinet["C-20"] = "조세호" # 새로운 값이 추가된다
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

cabinet.clear() # 사전에 있는 모든 값을 지운다
print(cabinet)