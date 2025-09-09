# c_num = input("전화번호를 입력하세요 >>>")
# if len(c_num) < 13 :
#     print(f"{c_num}유효하지 않은 전화번호 형식입니다.")
# else:
#     print(f"전화번호 중간 4자리는{c_num[4:8]}입니다.")
from sys import orig_argv


# num = int(input("몇개의 숫자를 입력하시겠습니까?>>>"))
# number = []
# number_a = 0
# number_b = 0
# number_c = 0
# for i in range(num):
#     number.append(int(input(f'{i + 1}번째 숫자를 입력하시오>>>')))
#     if number[i] > 0:
#         number_a += 1
#     elif number[i] < 0:
#         number_b += 1
#     else: number_c += 1
# print(f"양수:{number_a}")
# print(f"음수:{number_b}")
# print(f"0:{number_c}"

#     def __init__(self, name,student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = {}
#     def add_grade(self,subject,score):
#         self.grades[subject] = score
#     def get_average_grade(self):
#         return sum(self.grades.values())/len(self.grades)
# student1 = Student("김일",1)
# student1.add_grade("자바",60)
# student1.add_grade("파이썬",80)
# student1.add_grade("CSS",50)
# student1.add_grade("HTML",80)
# student1.add_grade("JS",80)
# print(f'학생이름 : {student1.name}')
# print(f'평균성적 : {student1.get_average_grade()}')
