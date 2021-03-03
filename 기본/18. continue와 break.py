absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue # 더이상 다음 문장을 실행시키지 안혹 다음 반복문을 실행시킨다.
    if student in no_book:
        print("{}: 선생님 책이 없어요".format(student))
        print("오늘 수업 여기까지. {0}는 남아라".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))






