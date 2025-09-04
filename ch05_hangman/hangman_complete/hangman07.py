import random
from hangman_arts import * # hangman_arts 파일의 전체 데이터를 가지고 온다는 의미
from hangman_word_list import word_list
chosen_word = random.choice(word_list)
display = []
lives = 6
for letter in range(len(chosen_word)):
    display.append("_")
end_of_game = False
print(logo)
while not end_of_game:
    print(stages[lives])
    print(' '.join(display))
    print(f'남은 목숨 {lives}')
    guess = input('알파벳을 입력하세요 >>>').lower()
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
        if lives == 0:
            print(logo)
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은{chosen_word}입니다.')
    if '_' not in display:
        print(logo)
        print('정답입니다.')
        end_of_game = True
        print(f'정답은{chosen_word}입니다.')
        break