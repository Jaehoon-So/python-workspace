# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))


menu = list(menu)
print(menu, type(menu)) # 메뉴의 타입이 리스트로 바뀌었다

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))