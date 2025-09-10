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