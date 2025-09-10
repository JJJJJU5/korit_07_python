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
    '커피' : 100,
}
logo = '''
SAMSUNG
'''
def is_resources_enough(order_ingredient):
    """
    DocString : 함수 / 클래스 / 메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능.
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후 , 음료 만들기가 가능하면 True 반환, 아니면 False 반환
    :param : order_ingredient
    :return: True/False
    """
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return  True
def process_coins():
    """동전을 입력 받아 전체 금액을 반환하는 함수 call3() 유형"""

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

def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 받은 동전의 총합이 음료 가격보다 높으면 True / 아니면 False를 반환, 그리고 True인 경우에는 profit에 음료 가격만큼 추가해줘야 하고, False인 경우에는 받은 동전들을 반환해주는 안내문 출력."""
    change = money_received - drink_cost
    if change >= 0:

        global profit
        profit += drink_cost
        print(f'잔돈 ${change}를 반환합니다.')
        return True
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
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'{drink_name}이 나왔습니다. 맛있게 드세요')

is_on = True

while is_on:
    print(logo)
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ').lower()
    if choice == 'report':
        for key in resources:
            print(f'남은 재료 {key}: {resources[key]}')
        print(f'수익 : ${profit}')
    elif choice == 'off':
        is_on = False
        print('자판기 사용이 종료되었습니다.')
    elif choice in ('에스프레소' , '라떼' , '카푸치노'):
        drink = MENU[choice]
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received=money_received, drink_cost=MENU[choice]['가격']):
                make_coffee(drink_name=choice, order_ingredient=drink['재료'])
    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요')
