'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(methods)
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def: define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값(outer)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미
3. (사용자) 함수의 형식 :
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return ...
변수 = 함수_이름(argument1 , argument2)
'''
# 함수 정의
# def display_name(name):
#     print(f'당신의 이름은 {name}입니다.')
#
# display_name('김일')
#
# def display_name_age(name,age):
#     print(f'당신의 이름은 {name}이고 나이는 {age}살 입니다.')
# display_name_age('김이',30)
# display_name_age(age=23,name='김삼') # keyword argument
'''
우리가 예를 들어 input('이름을 입력하세요 >>> ')을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name = input('이름을 입력하세요>>>')라고 작성해왔다.
그러면 여태까지 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있다. 파이썬 내장 함수는 이미 정의가 되어있고,
개발자들은 함수 호출만 잘하면 된다.

사용자 정의 함수의 경우 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 보면 된다.

내장 함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods): 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는
 함수. 사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있다.
함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''

# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하세요 >>>')
'''
이상의 코드는 함수 호출을 해서 그 결과값을 eng_name이라는 변수에 담았다고 볼 수 있따.

그리고 어제 수업한 것처럼 input()의 결과값의 자료형은 str이었다.
'''
# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
그렇다면 eng_name_upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는, str 자료형에 종속되어있다고 볼 수 있다.
그리고 그 결과값을, '다시 eng_name'이라는 변수에 담았기 때문에
51번 라인의 결과값과 53번 라인의 결과값이 차이가 생겼다.

함수(메서드)의 유형
'''
# 매개 변수 x / 리턴 x
def call1():
    print('[ x | x ]')
# 매개변수 o / 리턴 x
# def call2(unknown_parameter):
#     print('[ o | x ]')
#     print(f'{unknown_parameter}라고 입력함')
# def call3():
#     print('[ x | o ]')
#     return 1
# def call4(unknown1 , unknown2):
#     print('[ o | o ]')
#     return unknown1 + unknown2
# call1()
# call2("날씨")
# call2(1234)
# call3() # 결과값 : [ x | o ] 만 나옴
# print(call3())
# # 결과값 1
# print(call4("ㅎㅇ","ㅇㅇ"))
# print(call4(unknown2=1234, unknown1=456))


'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지
모든 경우의 수를 출력하도록 한다.

함수 정의
- 반환값 : 없음(call1 ~ call4 중 어떤 유형일지 고민 할 필요가 있다)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
def vending_machine(3000):

실행 예 
음료수 - 0개, 잔돈 = 3000원
음료수 - 1개 , 잔돈 = 2300원
...
음료수 - 4개 , 잔돈 = 200원
'''



# 1 for문으로 작성
# change = my_money - (drink_price * 음료개수)
# my_money를 기준으로 음료수를 살 수 있는 경우의 수를 고려했을 때 0 ~ 4개 까지 반복문이 5번이 돌아갑니다.


# def vending_machine():
#     my_money = int(input("지불 할 금액을 입력해주세요 >>> "))
#     drink_price = 700
#     for i in range(my_money//drink_price + 1):
#         print(f'음료수 개수 = {i}개, 잔돈 = {my_money-(drink_price*i)}')
#
# # 2 while문으로 작성
#
# def vending_machine2(money):
#     stock = 0
#     while money > 0:
#         print(f'음료수 {stock}개 잔돈 {money} ')
#         money -= 700
#         stock += 1
# vending_machine()

'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름: multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 : 
multiply(dan)  # argument가 dan
실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
...
3 x 9 = 27
'''
# for 버전
# call1()유형
# def multiply():
#     dan = int(input("몇 단을 출력하시겠습니까? >>> "))
#     for i in range(1,10):
#         print(f'{dan} x {i} = {dan * i}')
#
# multiply()
#
# while 버전
# call 1() 유형
# def multiply2():
#     dan = int(input("몇 단을 출력하시겠습니까? >>> "))
#     n = 1
#     while n < 10:
#         print(f'{dan} x {n} = {dan * n}')
#         n += 1
# multiply2()

# while 버전 call2() 유형
# def multiply3(dan):
#     n = 1
#     while n < 10:
#         print(f'{dan} x {n} = {dan * n}')
#         n += 1
#
# multiply3(5)

# for 버전 call2() 유형
# def multiply4(dan):
#     for i in range(1,10):
#         print(f'{dan} x {i} = {dan * i}')
# multiply4(500)


