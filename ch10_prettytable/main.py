'''
외부 패키지의 설치 #1 설정을 통한 방법
좌측 상단 메뉴버튼(햄버거)-> file -> settings(혹은 alt + ctrl + s)
좌측 상단 리스트에서 project: 프로젝트명 으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 #2 : 터미널을 이용하는 방법
alt + f12 눌러서 터미널 켠다
pip install prettytable
'''
from prettytable import PrettyTable

from pokemon_data import pokemon_data

table = PrettyTable()

table.field_names = ['번호' ,'이름' ,'타입']

# 1번 방법
# for Pokémon in pokemon_data:
#     table.add_row(Pokémon)

# 2번 방법
# table.add_rows(pokemon_data)

print(table)




