'''
# 지능형 시스템 과제 1 #
이름: 소재훈
학번: 20172638
전공: 컴퓨터학부
과목: 지능형 시스템 
'''

# 문제1:  5개의 이름, 학번으로 구성 된 "students"라는 이름의 Dictionary를 만든 후 출력
student = {'Jaehoon So': 20172638, 'Park': 20212222, 'Choi': 20213333, 'Lee': 20214444, 'Joo': 20215555}
print(student)

# 문제2: students Dictionary의 총 갯수 출력 (len 활용)
print(len(student))

# 문제3: 본인의 학번 출력 (Dictionary명과 본인의 이름(key) 사용하여 출력)
print(student['Jaehoon So'])

# 문제4: students Dictionary의 keys출력
print(student.keys())

# 문제5: students Dictionary의 values출력
print(student.values())