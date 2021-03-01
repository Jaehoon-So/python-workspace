python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python)) # 길이를 반환해준다. 17
print(python.replace("Python", "Java")) # Python 이라는 문자열을 찾아서 Java로 고쳐준다.

index = python.index("n") # n 이라는 글자가 어디에 위치해 있는지 나온다
print(index) # 5
index = python.index("n", index + 1) # index + 1 의 위치 에서부터 찾는다.
print(index) # 15

print(python.find("n"))
print(python.find("Java")) # -1 원하는 값이 없을 때는 -1을 반환해준다.
# print(python.index("Java")) # 오류