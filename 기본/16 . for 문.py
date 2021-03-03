print("대기번호: 1")
print("대기번호: 2")
print("대기번호: 3")
print("대기번호: 4")

# waiting_no 변수에 숫자 0~4까지 순서대로 들어간다.
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

# 0, 1, 2, 3, 4까지 no 에 들어가게 된다.
for no in range(5):
    print("대기번호: {0}".format(no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))