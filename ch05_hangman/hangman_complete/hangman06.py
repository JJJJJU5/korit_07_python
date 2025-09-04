import random
import hangman_word_list              # 이게 파일 명이라는 것에 주목
import hangman_arts                         # 해야한다
# 즉 logo / stages와 같은 변수가 아니다

# 외부의 hangman_word_list에 있는 word_list를 참조해서 우리는 chosen_word를 만들 필요가 있다

chosen_word = random.choice(hangman_word_list.word_list)
display = []
lives = 6
for letter in range(len(chosen_word)):
    display.append("_")
end_of_game = False
print(hangman_arts.logo)
while not end_of_game:
    print(hangman_arts.stages[lives])
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
            print(hangman_arts.logo)
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은{chosen_word}입니다.')
    if '_' not in display:
        print(hangman_arts.logo)
        print('정답입니다.')
        end_of_game = True
        print(f'정답은{chosen_word}입니다.')
        break