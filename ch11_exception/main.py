# Error_li = [(1, 'BaseException' , '최상위 예외 클래스'), (2, 'Exception' , '대부분 예외 클래스의 슈퍼 클래스'), (3,'AritmeticError','산술 연산에 문제가 있을 때'),
# (4,'AttributeError' , '잘못된 속성을 참조할 때'),(5,'E0FError','파일에서 더 이상 읽어 들일 데이터가 없을 때'),(6,'ModuleNotFoundError','import할 모듈이 없을 때'),
# (7,'FileNotFoundError','존재하지 않는 파일일 때'),(8,'IndexError','잘못된 인덱스를 사용할 때'),(9,'NameError','잘못된 이름(변수)를 사용할 때'),(10,'SyntaxError','문법이 틀렸을때'),
# (11,'TypeError','계산하려는 데이터의 유형이 잘못되었을 때'),(12,'ValueError','계산하려는 데이터 값이 잘못되었을때')]
'''
c11_exception
main

1. 예외 처리의 필요성
    1) 예외(exception) : 개발자가 직접 처리할 수 있는 문제
    2) 오류(error) : 개발자가 처리할 수 없는 문제

    3) 에외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해주는 것이 아니라, 발생된 문제로 인해
        프로그램이 비정상적으로 종료되는 것을 막고, 사용자에게 발생한 문제에 대해 정보를 전달하기 위함.


2. 예외 처리
    1) 고전적 예외 처리
    우리는 커피머신 오타 시 발생하는 오류를 해결하는 로직에서 사용했었다.
if drink == None:
    conti
3. 예외 처리의 종류
+------+---------------------+---------------------------------------------+
| 순번 |     예외 클래스     |                     의미                    |
+------+---------------------+---------------------------------------------+
|  1   |    BaseException    |              최상위 예외 클래스             |
|  2   |      Exception      |       대부분 예외 클래스의 슈퍼 클래스      |
|  3   |    AritmeticError   |          산술 연산에 문제가 있을 때         |
|  4   |    AttributeError   |           잘못된 속성을 참조할 때           |
|  5   |       E0FError      | 파일에서 더 이상 읽어 들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때           |
|  7   |  FileNotFoundError  |           존재하지 않는 파일일 때           |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때          |
|  9   |      NameError      |        잘못된 이름(변수)를 사용할 때        |
|  10  |     SyntaxError     |               문법이 틀렸을때               |
|  11  |      TypeError      |   계산하려는 데이터의 유형이 잘못되었을 때  |
|  12  |      ValueError     |     계산하려는 데이터 값이 잘못되었을때     |
+------+---------------------+---------------------------------------------+
4. 예외 처리 방식
    1) 모든 예외 처리하는 방식 -> try / except / finally
    형식:
try :
    코드 작성 영역
except : 
    예외 발생 시 처리 영역
finally :
    언제나 실행되는 영역
'''
import traceback
from traceback import print_tb

# try :
#     a = int(input("나누는 수 (제수)를 입력하세요 >>> "))
#     b = int(input("나누어지는 수 (피제수)를 입력하세요 >>> "))
#     print(f'b / a = {b / a}')
# except :
#     print("예외가 발생했습니다.")
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램이다.
try / except 문을 사용하여 '예외가 발생했습니다.' 를 출력할 수 있도록 작성하시오
'''
# try :
#     height = input('키를 입력하세요 >>> ')
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except :
#     print("예외가 발생했습니다.")
'''
    2) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가
        처리됨. 하지만 이상에서 본 것처럼, 0으로 나누는 경우와, str 자료형을 실수로 바꾸고자 하는 경우에 서로 다른 메시지를
        출력해줄 수 있다면, 개발자에게 예외를 처리할 수 있을만한 추가적인 정보를 제공할 수 있음.
        
        1)-1. 0으로 나누려고하는 경우 -> 0으로 나눌 수 없다다.
        1)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있다.
        등으로 특정 예외에 따른 서로 다른 안내문을 제시한다고 하면,
        except문 뒤에 처리하고자 하는 예외를 모두 명시하면 된다.
'''
# try :
#     a = int(input("나누는 수 (정수)를 입력하세요 >>> "))
#     b = int(input("나누어지는 수 (정수)를 입력하세요 >>> "))
#     print(f'b / a = {b / a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print("정수만 입력 할 수 있습니다.")
'''
    거의 모든 예외는 Exception 클래스의 서브 클래스에 해당함. 따라서 모든 예외는 Exception의 인스턴스가 된다.
    다음과 같이 except의 마지막에 Exception을 명시하면 예상하지 못한 예외들도 웬만하면 처리 된다.
    
형식 :
try :
    코드 작성 영역
except 예외 클래스1 :
    예외메세지
except 예외 클래스2:
    예외메세지2
...
except Exception:
    예외메세지n
finally:
    항시 실행되는 코드 영역

Java에서와 동일하게 Exception이 가장 상위에 있게 되면 모든 예외가 전부 Exception으로 잡히기 때문에 순서 역시 중요하다.

3. 예외 메세지 처리하기
    이상까지는 특정 예외가 발생했을때 메세지를 커스텀해서 사용했지만, 기본적으로 이미 예외 메세지를 가지고 있는 경우도 있다. default exception
    message를 출력하는 방식을 학습
    
형식 :
try :
    코드 작성 영역
except 예외클래스 as 예외메세지:
    예외 발생 시 처리 영역
'''
# z = [10,20,30,40,50]
#
# try :
#     print(z[10])
# except IndexError as e:
#     print(e)
'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데,
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계 없이 맨 마지막에 항상 처리되는 구문
'''
# try :
#     a = int(input("나누어지는 수를 정수로 입력하세요 >>>"))
#     b = int(input("나누는 수를 정수로 입력하세요 >>>"))
#     result = b / a         # 예외가 발생할 수 있는 구간이 try 문 내에 있어야만 한다.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(f'b / a = {result}')
# finally:
#     print("프로그램 종료")
'''
5. 강제로 예외를 발생시키기
    어떤 사람이 나이를 정수로 입력 받는 프로개름을 사용한다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않는다.( 그래서 우리는 0미만 200초과를 조건문으로 처리하는 것을 학습했다.)
    하지만 -1000살이 되는 것이 불가능하기 때문에 조건문이 아니라 직접 예외를 발생시켜서 처리하는 방법을 학습한다. -> raise문
형식 :
raise 예외클래스()

또는
raise 예외클래스(예외메세지)
raise의 경우 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는
 Exception이다.
'''
# age = int(input("나이를 입력하세요>>>"))           # - 100을 입력해도 예외가 발생되지 않는다.
# print(f'당신의 나이는 {age}살 입니다.')

# try :
#     age = age = int(input("나이를 입력하세요>>>"))
#     if age < 0 or age > 200:
#         raise Exception('강제로 발생시킨 예외입니다.')
# except Exception as e:
#     print("발생한 예외 메세지는 다음과 같습니다.")
#     print(e)
'''
이상은 특정 예외가 아니라 163번 으로 넘어가기만 해도 바로 예외가 발생해버린다.
즉 age에 가능한 정수값을 기입하더라도 예외가 발생하기 때문에 단독으로 처리가 안되는 것
그렇다면 이 부분에서는 조건문을 이용해서 특정 조건일 때만 예외로 넘기는 추가 코드가 필요하다고 할 수 있다.

6. 사용자 정의 예외 클래스

    음수를 입력 받을 때 강제로 예외를 발생시크는 예외 클래스를 정의
'''
# class NegativeAgeError(Exception):               # Exception 클래스를 상속 받았다는 의미
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
    # pass
# 예외를 발생시키기만 하면 되기 때문에 굳이 코드를 사용할 필요가 없어서
# Exception 클래스를 상속 받았으면 슈퍼 클래스의 속성/method를 사용할 수 있다.

# try :
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0:
#         raise NegativeAgeError('나이는 음수일 수 없습니다.')
#
# except NegativeAgeError as e:
#     print("발생한 예외 메세지는 다음과 같습니다.")
#     print(e)
# else:
#     print(f'당신의 나이는 {age}살입니다.')
#
# NegativeAgeError()

'''
과제 :
    나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜서 '200살 초과된 나이는 입력할 수 없습니다.'라는 메세지를 출력할 수 있도록 코드를 수정 .
'''
# class TooManyAgeError(Exception):
#     pass
# try :
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0:
#         raise NegativeAgeError('나이는 음수일 수 없습니다.')
#     if age > 200:
#         raise TooManyAgeError('200살 초과된 나이는 입력할 수 없습니다.')
#
# except NegativeAgeError as e:
#     print("발생한 예외 메세지는 다음과 같습니다.")
#     print(e)
# except TooManyAgeError as e:
#     print("발생한 예외 메세지는 다음과 같습니다.")
#     print(e)
# else:
#     print(f'당신의 나이는 {age}살입니다.')
# finally:
#     print('프로그램이 종료되었습니다.')
'''
과제

사용자의 점수를 0이상 100이하로 입력 받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는 프로그램을 작성하는데, 0이상 100 이하의 유효한 값이 아니라면 예외를 발생시키고
'점수는 0 이상 100이하 입니다' 라는 예외 메세지를 출력하시오 -> 사용자 정의 예외 클래스를 정의
ScoreOutOfRangeError 클래스로 정의

입력 받는데 예를 들어 백점이라고 입력하면 ' 점수는 숫자로 입력해야합니다' 라는 메세지를 출력하세요.
실수로 입력하면 ' 정수로 입력해야 합니다' 라는 메세지를 출력하세요.

예상할 수 없는 예외가 발생시 exception을 적용하여 디폴트 에러 메세지를 출력하세요.

프로그램이 종료되었다는 메세지를 맨 마지막에 작성하세요.
'''
# class ScoreOutOfRangeError(Exception):
#     pass
#
# try:
#     score = input("점수를 입력하세요 >>>")
#     score = int(score)
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError("0점과 100점 사이의 점수를 입력해주세요")
#     else:
#         if score > 80:
#             print("합격")
#         else:
#             print("불합격")
# except ScoreOutOfRangeError as e:
#     print(e)
# except ValueError:
#     print("점수는 숫자를 입력해주세요")
#
# except TypeError :
#     print("점수는 실수로 입력해주세요")
#
# except Exception as e:
#     print(e)
# else:
#     print(f'당신의 점수는 {score} 입니다.')
# finally:
#     print("프로그램 종료")

'''
사용자로부터 숫자를 입력 받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 에외 메세지를 출력하시오.

지시 사항
1. 사용자로부터 숫자를 입력 받는다.
2. 입력받은 숫자로 100을 나누어 결과를 출력한다.
3. 입력 값이 0일 경우 적절한 예외를 처리하여 '0'으로 나눌수 없습니다'라는 메세지를 출력한다.
4. 입력 값이 숫자가 아닌 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다' 라는 메세지를 출력한다.
5. 예외가 발생하지 않는 경우 '정상적으로 처리되었습니다.' 라는 메세지를 출력하고, 결과도 출련한다.
6. 프로그램 종료 메세지를 출력한다.
'''


# try :
#     num = int(input("100을 나눌 숫자를 입력하세요 >>> "))
#     num2 = 100 / num
# except ValueError:
#     print("숫자만 입력할 수 있습니다.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f'100 / {num} = {num2}입니다.')
#     print('정상적으로 처리되었습니다.')
#
# finally:
#     print("프로그램을 종료합니다.")

'''
사용자로부터 리스트의 인덱스를 입력 받아 해당 인덱스의 값을 출력하는 프로그램을 작성하시오.
만약 잘못된 인덱스를 입력하면 적적ㄹ한 에외 메세지를 출력하시오.

지시 사항
1. 미리 정의된 리스트가 있다.
2. 사용자로부터 리스트의 인덱스를 입력 받는다.
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력한다.
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메세지를 출력한다.
5. 사람을 의심하고 예상되는 예외를 적용한다.
6. 예외가 발생하지 않는 경우 "정상적으로 처리되었습니다"라는 메세지와 함께 해당 인덱스의 값을 출력한다.
7. 프로그램 종료 메세지를 출력한다.
8. 마이너스인덱스는 적용시키지 않는다. -> 사용자 정의 예외 클래스를 통해서 적용한다.
    -> NegaviceNumIndexError라고 이름 짓고 처리한다.
'''
# my_list = [10,20,30,40,50]
# c_list = []
# class NegativeNuminousesError(Exception):
#     pass
#
# try :
#     n = input("인덱스 넘버를 입력하세요 >>>")
#     n = int(n)
#     if n <= 0:
#         raise NegativeNuminousesError("")
#     for my_num in range(n):
#         c_list.append(my_list[my_num]*2)
# except NegativeNuminousesError as e:
#     print(e)
# except IndexError:
#     print("IndexError")
# except ValueError:
#     print("ValueError")
# except Exception as e:
#     print("예상할 수 없는 예외가 발생했습니다.")
#     print(e)
# else:
#     print(c_list)
# finally:
#     print("종료")
'''
만약 사용자가 잘못된 속성을 입력하면 적절한 예외 처리 메시지를 출력하시오.

지시 사항
1. 미리 정의된 클래스와 객체가 있다.
2. 사용자로부터 속성명을 입력받는다.
3. 입력받은 '속성명'을 사용하여 객체의 '속성값'을 출력한다.
4. 잘못된 속성명을 입력하면 ' 존재하지 않는 속성입니다' 라는 메세지를 출력한다.
5 예외가 발생하지 않은 경우 '정상적으로 처리되었습니다' 라는 메세지와 속성값을 출력한다.
6. 프로그램 종료 메세지를 출력한다.
'''
class Person:
    sc = "KORIT"
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
person2 = Person(name="호날두",age=40)
# print(vars(person2)) # vars(객체명) : 객체의 속성명 - 값을 dictionary로 만들어준다. JSON과 유사.
# print(getattr(person2,'name')) # getattr()의 두 번째 argumnet는 인스턴스 변수명을 받는다. -> 그 데이터를 str으로 받는다

# try:  # 내가 한것
#     R7 = input("속성명을 입력하세요 >>>")
#     R9 = getattr(person2, R7)
# except AttributeError as e:
#     print('존재하지 않는 속성입니다.')
# except Exception as e:
#     print('예상 할 수 없는 예외')
#     print(e)
# else:
#     print(R9)
#     print("정삭적으로 처리되었습니다.")
# finally:
#     print("종료")
person1_dict = vars(person2)
'''
getattr(객체명,  속성명_str) - 특정 객체의 두번째 argument와 일치하는 속성명의 값을 return
vars(객체명) - 특정 객체의 속성명 - 속성값 쌍을 dictionary 형태의 key - value 쌍으로 변환
'''
print(person1_dict)
attr_key = input("출력할 속성명을 입력하세요 >>> ")
print(person1_dict[attr_key])
