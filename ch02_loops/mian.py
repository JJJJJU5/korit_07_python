'''
1. while 반복문
    while 다음에 오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건문이 False가 될 때까지)
형식 :
while 조건식1:
    반복실행문

특정 시점에 while 반목문이 종료될 수 있도록 지정해야한다
'''
# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 +=1               # python에는 ++가 없다.


'''
기본 예제 
10부터 1까지 역순을 ㅗ출력
'''
# n2 = 10
# while n2 > 0:
#     print(n2)
#     n2 -= 1

'''
중첩 while 문 (while문 뿐만 아니라 내부에 if를 쓸 수도 있다)
중첩 while 및 f-string을 활용하여 구구단 만들기
dan = 1
num = 1
while dan <= 9:
    while num <= 9:
        print(f'{dan} X {num} = {dan * num}')
        num += 1
    dan += 1
    num = 1

'''
dan = 1
num = 1
while dan <= 9:
    while num <= 9:
        print(f'{dan} X {num} = {dan * num}')
        num += 1
    dan += 1
    num = 1

# while dan <= 9:
#     num = 1
#     while num <= 9:
#         result = dan * num
#         print(f'{dan} X {num} = {result}')
#         num += 1
#     dan += 1

