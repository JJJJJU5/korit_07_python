from menu import  Menu
from coffee_maker import  CoffeeMaker
from money_machine import  MoneyMachine
# python 객체 만드는 방식 이전과 차이가 있다면 외부 모듈에서 가지고 온 클래스의 객체를 생성했다는 점 . Scanner scanner = new Scanner(System.in)과 동일한 방식
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# coffee_maket / money_machine / menu 모듈은 하나도 안건드리고 main에만 코드를 작성해서 pop version과 동일한 기능을 하는 coffee_machine을 만들기
is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? ({menu.get_items()}) >>> ')
    if choice == 'off':
        is_on = False
        print('작동을 중지합니다.')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
       drink = menu.find_drink(choice)
       if drink == None:  # chioce에 오타가 있을 경우 None이 반환되기 대문에 고전적 예외처리
           continue
       if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)



       # 조건문을 이용해 process_coins()와 make_payment()를 활용하여,
       # 모든 것이 true일대 '작동 중입니다'를 출력 할 수 있도록 작성하시오.
    # 음료 이름을 입력 받은 시점부터 프로세스를 떠올려서 코드를 작성해야만 한다. 이때 까지 고려할 것은 절차지향 방식으로 코딩했을 때의 과정과
