year = int(input("윤년인지 확인하고 싶은 연도를 입력하세요 >>>"))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'{year}년도는 윤년입니다')
# else:
#     print(f'{year}년도는 윤년이 아닙니다.')

if year % 4 == 0 :
    if year % 100 != 0 :
        if year % 400 == 0 :
            print(f'{year}는 윤년 입니다.')
        else:
            print(f'{year}년도 윤년이 아닙니다.')
    else:
        print(f'{year}년도 윤년이 아닙니다.')
else:
    print(f'{year}년도 윤년이 아닙니다.')
'''
중첩 if문을 사용한 풀이 방식



논리 연산자를 사용한 풀이 방식
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year}년도는 윤년입니다')
else:
    print(f'{year}년도는 윤년이 아닙니다.')
'''