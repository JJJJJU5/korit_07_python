import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있다.
'''
# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하기
lives = 6
# todo - 2 : hangman03을 참조하여 while 반복문 바깥을 완성하시오.
word_list = ['apple' , 'banana' , 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in range(len(chosen_word)):
    display.append("_")
# todo - 3 : while문의 조건을 수정하여  6 번의 기회가 소진되면 반복문이 종료될 수 있도록 작성하시오.
# else:
            #     lives -= 1
            #     if lives == 0:
            #         end_of_game = True # 라고 작성하면 안된다. 반복문 내부에서 guess가 일치하는지 여부를 따지는 중이다. 예를 들어 chosen_word가 apple이고, guess가 a라고 가정했을 때 첫번째 반복에서는 display의 0번지가 a로 바뀐다. 그런데 반복문 내부에 위치해 있기 때문에 1,2,3,4번지에 대해서도 a가 display의 인덱스와 일치하는 element인지를 확인하게 된다. 그 결과 p p l e가 a와 다르기 때문에 lives -= 1이 4번 적용되어서 맞는 답을 입력했음에도 불구하고 행맨이 완성되는 것을 확인할 수 있게 된다            # 이상의 이유로 for 반복문 바깥에서 guess가 chosen_word에 속하지 않는지를 확인하는 조건문을 '별개로' 작성해야만 한다.

end_of_game = False

while not end_of_game:    # 어느 시점에 end_of_game = True
    guess = input('알파벳을 입력하세요 >>>').lower()
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
        print(stages[lives])
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은{chosen_word}입니다.')
    if '_' not in display:
        print('정답입니다.')
        end_of_game = True   # 이 시점에 end_of_game이 True가 되었으므로 다음 반복문이 실행되지 않음 -> 96번 코드라인이 실행된다는 것을 의미한다.
        print(f'정답은{chosen_word}입니다.')
        break                 # 바로 반복문 정지 -> 98번 코드라인 실행 x

    # 현재 상황이 콘솔창에 출력돼서 user에게 안내가 가면 좋겠다
    print(' '.join(display))
# todo - 4 : lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때 마다 올바른 stages의 element가 출력될 수 있도록 작성하시오.

# 현재 기준에서 아까 완성판과 차이점 : logo 유무 / word_list가 부족함/ 혹시나 리팩토링 가능한지 여부
# hangman05 파일 생성 -> 필요한 부분들 다 복사하고 주석들 다 지워서 정리 해놓기
# logo를 text to ascil arts를 검색해서 하나 받아와서 맨 처음에 로고를 출력할 수 있도록 코드를 작성한다.
