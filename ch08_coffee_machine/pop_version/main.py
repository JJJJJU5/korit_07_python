from tkinter import Menu
from traceback import print_tb

MENU = {
    '에스프레소' : {
        '재료': {
            '물': 50 ,
            '커피': 10,
        },
        '가격': 1.5,
    },
    '라떼' : {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격' : 3.0,
    },
}
# 실행 예ㅇ
# 라고 콘솔 출력할 수 있도록 카푸치노의 우유량을 추출하는 코드를 작성하시오.

# 에스프레소의 가격을 추출하시오.

# 라떼의 재료 이름만 출력하시오.
# print(f'카푸치노에 우유가 {MENU["카푸치노"]['재료']["우유"]}ml가 들어갑니다.')
# print(f'{MENU["에스프레소"]["가격"]}')
# for i in MENU['라떼']['재료'].keys():
#     print(i, end=" ")
'''
에스프레소 / 라떼 / 카푸치노를 50잔씩 만든다고 가정했을 때 필요한
커피 / 우유 / 물의 양은 얼마인가?
'''
# print(MENU['에스프레소']['재료']['물']*50+MENU['라떼']['재료']['물']*50+MENU['카푸치노']['재료']['물'] *50)
# print(MENU['에스프레소']['재료']['커피']*50+MENU['라떼']['재료']['커피']*50+MENU['카푸치노']['재료']['커피']*50 )
# print(MENU['라떼']['재료']['우유']*50+MENU['카푸치노']['재료']['우유']*50 )
coffee = 0
water = 0
milk = 0
# for key in MENU:
#     for key_key in MENU[key]['재료']:
#         if key_key == '커피':
#             coffee += MENU[key]['재료'][key_key]
#         elif key_key == '물':
#             water += MENU[key]['재료'][key_key]
#         else:
#             milk += MENU[key]['재료'][key_key]
for i in MENU:
    # print(i)
    # print(MENU[i])
    for ii in MENU[i]['재료']:
        # print(ii)
        # print(MENU[i]['재료'][ii])
        if ii == '커피':
            coffee += MENU[i]['재료'][ii]
        elif ii == '물':
            water += MENU[i]['재료'][ii]
        else:
            milk += MENU[i]['재료'][ii]




print(coffee*50)
print(water*50)
print(milk*50)
'''
이상의 학습 과정에서 중요한 부분은 중첩적으로 이루어진 dictionary - JSON - 기타 collections들이 합쳐진
데이터에서 내가 필요한 부분을 어떻게 추출할 수 있을까 이다.

일반적으로는 list의 경우 index를 이용하기 때문에 반복문을 쓰고 치우면 그만인데 반해 dictionary는 반복문을 돌리면 key가 나오게 되고,
그 key를 또 이용해야지만 value가 추출된다.

그리고 그 value를 이용해서 연산을 하거나 로직을 작성해야 한다.
근데 value가 또 dictionary거나 list거나 혹은 객체거나 한 경우에는 좀 복잡하게 된다.
이를 연습하기 위한 수업이었고, coffee_machine을 작성하면서 중첩 dictionary를 활용했다.
'''
MENU = {
    '에스프레소' : {
        '재료': {
            '물': 50 ,
            '커피': 10,
        },
        '가격': 1.5,
    },
    '라떼' : {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격' : 3.0,
    },
}

profit = 0
resources = {
    '물' : 300,
    '우유' : 200,
    '커피' : 200,
}

# 함수 정의 영역
# 커피 로직 정의
def is_resources_enough(order_ingredient): # 만약 특정 함수 / 메서드의 결과값이 boolean이라면 대개 다음 조건문 / 반복문의 조건식으로 쓰이는 경우가 많다 . 함수형 프로그래밍 개념을 떠올리면 된다.
    """
    DocString : 함수 / 클래스 / 메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능.
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후 , 음료 만들기가 가능하면 True 반환, 아니면 False 반환
    :param : order_ingredient
    :return: True/False
    """
    for item in order_ingredient:       # order_ingredient의 자료형은 무엇이고 그 근거는 ? dict resources가 dict이고 for 반복문을 돌리면 key가 뽑아져 나오기 때문
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return  True
def process_coins():
    """동전을 입력 받아 전체 금액을 반환하는 함수 call3() 유형"""
    # 쿼터, 다임, 니켈 , 페니 네 종류의 동전
    '''
    쿼터 = 0.25 달러               quarter
    다임 = 0.1 달러                dime 
    리켈 - 0.05 달러               nickel    
    페니 0.01 달러                 penny
    '''
    sum = 0
    # 이 부분에 로직이 작성되어야 한다.
    sum += float(input('쿼터 동전을 몇 개나 넣으시겠습니까? >>> ')) *0.25
    sum += float(input('다임 동전을 몇 개나 넣으시겠습니까? >>> ')) *0.1
    sum += float(input('니켈 동전을 몇 개나 넣으시겠습니까? >>> ')) *0.05
    sum += float(input('페니  동전을 몇 개나 넣으시겠습니까? >>> ')) *0.01
    return sum
 # todo - 6 :왜 동전 처리 함수를 정의했는지 이해를 하고 해당 총합을 가지고 총합이 '선택한' 음료의 가격보다 높으면 다음 과정으로 넘어갈 필요가 있다.
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 받은 동전의 총합이 음료 가격보다 높으면 True / 아니면 False를 반환, 그리고 True인 경우에는 profit에 음료 가격만큼 추가해줘야 하고, False인 경우에는 받은 동전들을 반환해주는 안내문 출력."""
    change = money_received - drink_cost
    if change >= 0:
        # 이러면 음료 제조 과정으로 넘어가야된다. 그리고 profit에도 추가해야 함.
        global profit # 전역 변수인 profit을 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost # 근데 함수 호출을 통한 전역 변수의 값 변화는 권장하지 않는 방법
        print(f'잔돈 ${change}를 반환합니다.')
        return True # True로 해야 음료 제조 과정의 조건식으로 사용 할 수 있음.
    else:
        print(f"금액이 충분하지 않습니다. ${money_received}를 반환합니다.")
        return False

def make_coffee(drink_name , order_ingredient):
    """
    resources에 있는 재료에서 메뉴['음료명']['재료']들을 차감함.
        -> 차감은 is_resources_enough()이 True였기 때문에 무조건 0 이상이 나온다.
    :param drink_name: str
    :param order_ingredient: dict
    :return: none -> call2
    """
    for item in order_ingredient:                # resources가 아니라 order_ingredient를 반복문을 돌리는 이유는 에스프레소 일 때 오류가 발생하기 때문이다. 에스프레소의 재료에는 우유가 들어가지 않아 resorces에 있는 key인 우유와 만나면 오류가 발생한다.
        resources[item] -= order_ingredient[item]
    print(f'{drink_name}이 나왔습니다. 맛있게 드세요')
'''
현재 자판기 내에 있는 물 / 우유 / 커피 / 금액에서 라떼 한잔을 뽑고 나서의 물 / 우유 / 커피 / 금액의 변동을 콘솔에 출력하시오.
실행 예
물 : xml
우유 : xml
커피 : xg
수익 : $x
'''
profit += MENU['라떼']['가격']

# for resource in resources:
#     resources[resource] -= MENU['라떼']['재료'][resource]
#     if resource == '커피':
#         print(f'{resource}:{resources[resource]}g')
#     if resource == '물':
#         print(f'{resource}:{resources[resource]}ml')
#     if resource == '우유':
#         print(f'{resource}:{resources[resource]}ml')
#


#todo - 2 : 커피 머신이 반복적으로 돌가야하는데, off를 입력 받으면 종료가 이루어져야 한다.

# 관련 변수 선언 및 초기화
is_on = True
while is_on:
    # 반복문 내부에서  입력 받아야 하니까 여기에 선언 및 초기화
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ').lower()
    # 만약에 choice 변수에 들어간 데이터가 'off'라면 반복문을 종료하도록 코드를 작성
    # todo - 3 : 사용자가 프롬프트에 "report"를 입력하면 현재 자원 값을 보여주는 보고서를 생성한다.
    if choice == 'report':
        for key in resources:
            print(f'남은 재료 {key}: {resources[key]}')
        print(f'돈 : ${profit}')
    elif choice == 'off':
        is_on = False
        print('자판기 사용이 종료되었습니다.')
    # todo - 4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나 일대 작성하는 부분

    # todo - 5 : choice가 이상의 조건을 충족하지 않을 때 '잘못 입력하셨습니다. 다시 입력하세요'를 출력하는 부분
    #elif choice == '에스프레소'  or choice == '라떼' or choice == '카푸치노': 자바형식
    elif choice in ('에스프레소' , '라떼' , '카푸치노'):
        print('')
        if is_resources_enough(MENU[choice]['재료']):
            money_received = process_coins()
            # 여기의 money_received는 전역 변수이다. 그리고 process_coins()의 결과값을 변수에 담았다.
            if is_transaction_successful(money_received=money_received, drink_cost=MENU[choice]['가격']):
                make_coffee(drink_name=choice, order_ingredient=MENU[choice]['재료'])

    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요')